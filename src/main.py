
from flask import Flask
from flask_cors import CORS
from flask import request
import requests as r
from set_envs import API_URL

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def health():
    return {'status': 'status', 'message': 'tô vivo'}, 200

@app.route('/bater-ponto', methods=['POST'])
def baterPonto():

    data = request.get_json(force=True)

    try:
        include_at = data.get('includedAt', None)
        employeeId = data.get('employeeId', None)
        employerId = data.get('employerId', None)

        if include_at == None or employeeId == None or employerId == None:
            return {'status': 422, 'response': 'Preencha todos os campos'}, 422 
    except Exception as e:
        print(e)
        
    request_body = {
        'includedAt': include_at,
        'employeeId': employeeId,
        'employerId': employerId
    }

    response = r.post(f'{API_URL}/proxy/ab2198a3-cafd-49d5-8ace-baac64e72222', json=request_body)

    if response.status_code != 200:
        return {'status': str(response.status_code), 'response': response.json(), 'request':request_body}, int(response.status_code)

    return {'status': response.status_code, 'response': str(response.json())}, 200


if __name__ == '__main__':
    app.run(host="::", port=5000)