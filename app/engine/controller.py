import os
from flask import Flask, jsonify
from models import User, Product, Category, City
from service import getUserInfo
import neomodel



def create_app():
    """ app start point and API endpoing """
    
    app = Flask(__name__)
    neomodel.config.DATABASE_URL = os.environ['NEO4J_BOLT_URL']

    @app.route('/user/<id>', methods=['GET'])
    def handler(id):
        return getUserInfo(id)
        
    return app


if __name__ == "__main__":

    flask_app = create_app()
    flask_app.run(debug=True)
