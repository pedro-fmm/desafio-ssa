from flask import Blueprint
from flask_restful import Api

# import components
from components.health import Health
from components.bater_ponto import BaterPonto

api_blueprint = Blueprint("", __name__)
api = Api(api_blueprint)

api.add_resource(Health, '/')
api.add_resource(BaterPonto, "/bater-ponto")