import os
from flask import Flask, jsonify
from service import getUserInfo, getUserReco



def create_app():
    """ app start point and API endpoing """
    
    app = Flask(__name__)
    neomodel.config.DATABASE_URL = os.environ['NEO4J_BOLT_URL']

    @app.route('/user/<id>', methods=['GET'])
    def handler(id):
        """ endpoint to request user info and orders """
        return getUserInfo(id)

    @app.route('/user/recomended/<id>', methods=['GET'])
    def handler(id):
        """ endpoint to request user recomendations """
        return getUserReco(id)
        
    return app


if __name__ == "__main__":

    flask_app = create_app()
    flask_app.run(debug=True)
