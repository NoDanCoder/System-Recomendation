import neomodel
from models import User, Product, Category, City


def getUserInfo(id):
    """ Return user info and history of ordered products """
    instance = User.nodes.first(uuid=id)
    products = instance.order.all()
    instance = instance.to_dict()
    instance['products'] = [x.to_dict() for x in products]
    return instance


def getUserReco(id):
    """ Return user recomendated products based on previous orderers
        or related users orders
    """
    return 'user reco'