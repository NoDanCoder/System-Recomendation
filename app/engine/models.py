from neomodel import (
    StructuredNode, 
    StructuredRel, 
    StringProperty, 
    UniqueIdProperty, 
    EmailProperty, 
    IntegerProperty, 
    RelationshipTo, 
    RelationshipFrom
)


# Relation model classes

class BelongsToRel(StructuredRel):
    """ Belongs_to relation class
        On db:
            (:Product)-[:BELONGS_TO]->(:Category)
    """
    pass


class OrderRel(StructuredRel):
    """ Order relation class
        On db:
            (:User)-[:ORDER]->(:Product)
    """
    
    times = IntegerProperty()


class SupplyRel(StructuredRel):
    """ Supply relation class
        On db:
            (:User)-[:SUPPLY]->(:Category)
    """
    pass

class LivesInRel(StructuredRel):
    """ Lives_In relation class
        On db:
            (:User)-[:LIVES_IN]->(:City)
    """
    pass


# Node model classes

class User(StructuredNode):
    """ User node class """

    uuid = UniqueIdProperty()
    name = StringProperty(unique_index=True, required=True)

    order = RelationshipTo('Product', 'ORDER', model=OrderRel)
    supply = RelationshipTo('Category', 'SUPPLY', model=SupplyRel)
    lives_in = RelationshipTo('City', 'LIVES_IN', model=LivesInRel)


    def to_dict(self):
        """ Call to get main data to directly handle it """
        return {
            "uuid": self.uuid,
            "name": self.name
        }

class Product(StructuredNode):
    """ Product node class """

    uuid = UniqueIdProperty()
    name = StringProperty(unique_index=True, required=True)
    description = StringProperty(required=True)
    image = StringProperty()

    belongs_to = RelationshipTo('Category', 'BELONGS_TO', model=BelongsToRel)

    
    def to_dict(self):
        """ Call to get main data to directly handle it """
        return {
            "uuid": self.uuid,
            "name": self.name,
            "description": self.description,
            "image": self.image
        }

class Category(StructuredNode):
    """ Catergory node class """

    uuid = UniqueIdProperty()
    name = StringProperty(unique_index=True, required=True)
    

    def to_dict(self):
        """ Call to get main data to directly handle it """
        return {
            "uuid": self.uuid,
            "name": self.name
        }


class City(StructuredNode):
    """ City node class """

    uuid = UniqueIdProperty()
    name = StringProperty(unique_index=True, required=True)
    countryCode = StringProperty(unique_index=True, required=True)


    def to_dict(self):
        """ Call to get main data to directly handle it """
        return {
            "uuid": self.uuid,
            "name": self.name,
            "countryCode": self.countryCode
        }