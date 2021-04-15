import neomodel
from models import User, Product, Category, City


def getUserInfo(id):
    instance = User.nodes.first(uuid=id)
    products = instance.order.all()
    instance = instance.to_dict()
    instance['products'] = [x.to_dict() for x in products]
    return instance