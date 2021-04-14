from neomodel import StructuredNode, StringProperty, UniqueIdProperty, EmailProperty


class User(StructuredNode):

    uuid = UniqueIdProperty()
    name = StringProperty(unique_index=True, required=True)

class Product(StructuredNode):

    uuid = UniqueIdProperty()
    name = StringProperty(unique_index=True, required=True)
    descripcion = StringProperty(required=True)
    image = StringProperty()

class Catergory(StructuredNode):

    uuid = UniqueIdProperty()
    name = StringProperty(unique_index=True, required=True)

class City(StructuredNode):

    uuid = UniqueIdProperty()
    name = StringProperty(unique_index=True, required=True)
    countryCode = StringProperty(unique_index=True, required=True)