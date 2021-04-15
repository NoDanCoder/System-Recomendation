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
    pass


class OrderRel(StructuredRel):
    
    times = IntegerProperty()


class SupplyRel(StructuredRel):
    pass

class LivesInRel(StructuredRel):
    pass


# Node model classes

class User(StructuredNode):
    """ User node class """

    uuid = UniqueIdProperty()
    name = StringProperty(unique_index=True, required=True)

    order = RelationshipTo('Product', 'ORDER', model=OrderRel)
    supply = RelationshipTo('Category', 'SUPPLY', model=SupplyRel)
    lives_in = RelationshipTo('City', 'LIVES_IN', model=LivesInRel)

class Product(StructuredNode):
    """ Product node class """

    uuid = UniqueIdProperty()
    name = StringProperty(unique_index=True, required=True)
    descripcion = StringProperty(required=True)
    image = StringProperty()

    belongs_to = RelationshipTo('Category', 'BELONGS_TO', model=BelongsToRel)

class Category(StructuredNode):
    """ Catergory node class """

    uuid = UniqueIdProperty()
    name = StringProperty(unique_index=True, required=True)


class City(StructuredNode):
    """ City node class """

    uuid = UniqueIdProperty()
    name = StringProperty(unique_index=True, required=True)
    countryCode = StringProperty(unique_index=True, required=True)