from flask_restful import Resource
from flask import request
import requests
from datetime import datetime

from .set_envs import API_URL


class BaterPonto(Resource):

    def post(self):

        data = request.get_json(force=True)

        include_at = data.get('includedAt', None)
        if include_at == None:
            include_at = datetime.timestamp(datetime.now())
        employeeId = data.get('employeeId', None)
        employerId = data.get('employerId', None)

        if include_at == None or employeeId == None or employerId == None:
            return {'status': 422, 'response': 'Preencha todos os campos'}, 422 

        request_body = {
            'includedAt': include_at,
            'employeeId': employeeId,
            'employerId': employerId
        }

        response = requests.post(f'{API_URL}/proxy/ab2198a3-cafd-49d5-8ace-baac64e72222', json=request_body)

        if response.status_code != 200:
            return {'status': str(response.status_code), 'response': response.json(), 'request':request_body}, int(response.status_code)

        return {'status': response.status_code, 'response': response.json()}, 200