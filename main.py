import boto3
from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

ddb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000', region_name='us-west-2', aws_access_key_id="N/A",
                          aws_secret_access_key="N/A")
tablaCaras = ddb.Table('Caras')


@app.route('/agregarCara', methods=['POST'])
def agregar_cara():
    data = request.json
    item = {
        'name': data['name'],
        'descriptors': [str(x) for x in data['descriptors']]
    }
    tablaCaras.put_item(Item=item)
    return jsonify(item)


@app.route('/getCaras', methods=['GET'])
def get_caras():
    result = tablaCaras.scan()['Items']
    return jsonify(result)

if __name__ == '__main__':
    app.run()