import os
from flask import Flask, jsonify
from flask_cors import CORS
from service import getUserInfo, getUserReco, getUserRecoOthers
import neomodel


def create_app():
    """ app start point and API endpoing """
    
    app = Flask(__name__)
    neomodel.config.DATABASE_URL = os.environ['NEO4J_BOLT_URL']
    CORS(app)

    @app.route('/user/<id>', methods=['GET'])
    def handlerUser(id):
        """ endpoint to request user info and orders """
        return getUserInfo(id)

    @app.route('/user/reco-category/<id>', methods=['GET'])
    def handler_reco_category(id):
        """ endpoint to request user recomendations based on
            categories popularity
        """
        return getUserReco(id)

    @app.route('/user/reco-users/<id>', methods=['GET'])
    def handler_reco_users(id):
        """ endpoint to request user recomendations based on
            customers similarity
        """
        return getUserRecoOthers(id)
    
    return app


if __name__ == "__main__":

    flask_app = create_app()
    flask_app.run(debug=True)
