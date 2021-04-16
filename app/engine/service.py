from flask import jsonify
import neomodel
from models import User, Product, Category, City


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
                    .uuid, .name, .description
                })
            }
    """
    
    response = neomodel.db.cypher_query(cyper_query, {"uuid": id})
    return jsonify([ elem[0] for elem in response[0] ])


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
                categor: (c{
                    .uuid, .name, 
                    product: (p{
                        .uuid, .name, .description
                    })
                })
            }
    """
    response = neomodel.db.cypher_query(cyper_query, {"uuid": id})
    return jsonify([ elem[0] for elem in response[0] ])


def getUserRecoOthers(id):
    """ Return user recomendated products based on similar
        cusromers behavior, ordered by similarity of consumption between customers
        on the same target
    """
    
    cyper_query = """
        MATCH (u:User {uuid: $uuid})-[:ORDER]->(:Product)<-[:ORDER]-(:User)-[:ORDER]->(p:Product)
        WHERE NOT (u)-[:ORDER]->(p) AND (p)-[:BELONGS_TO]->(:Category)<-[:SUPPLY]-(u)
        WITH p, u, COUNT(p) AS times ORDER BY times DESC
        RETURN
            u{
                .uuid, .name,
                product: (p{
                    .uuid, .name, .description
                })
            }
    """
    
    response = neomodel.db.cypher_query(cyper_query, {"uuid": id})
    return jsonify([ elem[0] for elem in response[0] ])