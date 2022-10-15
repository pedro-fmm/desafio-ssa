
from flask import Flask
from flask_cors import CORS
from endpoints import api_blueprint


if __name__ == '__main__':
    app = Flask(__name__) # create app
    CORS(app) # set cors
    
    app.register_blueprint(api_blueprint, url_prefix="/") # set api blueprint
    
    app.run(host="::", port=5000) # run with parameters
