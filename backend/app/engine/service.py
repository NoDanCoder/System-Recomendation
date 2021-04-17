from flask import jsonify
import neomodel
from models import User, Product, Category, City


def errorMesage():
    return {'error': 'user with given id does not exist'}


def formatOutput(function):
    """ decorator to handle cypher query requests and return json format """

    def wrapper(id):
        if not User.nodes.first_or_none(uuid=id):
            return errorMesage()
        
        cypher_query = function(id)
        response = neomodel.db.cypher_query(cypher_query, {"uuid": id})
        return jsonify([ elem[0] for elem in response[0] ])

    return wrapper


@formatOutput
def getUserInfo(id):
    """ Return user info and history of ordered products
        ordered by most bought
    """
    
    cyper_query = """
        MATCH (u:User {uuid: $uuid})-[o:ORDER]->(p:Product)
        WITH u, p, sum(o.times) AS add ORDER BY add DESC
        RETURN 
            u{
                .uuid, .name,
                product: (p{
                    .uuid, .name, .description, .image
                })
            }
    """

    return cyper_query


@formatOutput
def getUserReco(id):
    """ Return user recomendated products based on previous orderers
        or related users orders, ordered by popularity
    """
    
    cyper_query = """
        match (u:User {uuid: $uuid})-[:SUPPLY]->(c:Category)<-[:BELONGS_TO]-(p:Product)<-[o:ORDER]-(:User)
        WITH u, c, p, sum(o.times) AS add ORDER BY add DESC
        RETURN 
            u{
                .uuid, .name,
                category: (c{
                    .uuid, .name, 
                    product: (p{
                        .uuid, .name, .description, .image
                    })
                })
            }
    """

    return cyper_query


@formatOutput
def getUserRecoOthers(id):
    """ Return user recomendated products based on similar
        cusromers behavior, ordered by similarity of consumption between customers
        on the same target
    """
    
    cyper_query = """
        MATCH (u:User {uuid: $uuid})-[:ORDER]->(:Product)<-[o:ORDER]-(ru:User)
        WITH u, ru, count(o) * sum(o.times) AS score

        MATCH (ru)-[op:ORDER]->(p:Product)
        WHERE NOT (u)-[:ORDER]->(p) and (p)-[:BELONGS_TO]->(:Category)<-[:SUPPLY]-(u)
        WITH u, p, ru, score * op.times AS score ORDER BY score DESC
        WITH u, p, count(p) AS connectedNodes, sum(score) AS endScore
        WITH u, p, connectedNodes * endScore AS score ORDER BY score DESC
        RETURN             
            u{
                .uuid, .name,
                product: (p{
                    .uuid, .name, .description, .image
                })
            }
    """

    return cyper_query