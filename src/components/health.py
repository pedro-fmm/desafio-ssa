from flask_restful import Resource


class Health(Resource):
    def get(self):
        return {'status': 'success', 'message': 'i\'m alive'}, 200