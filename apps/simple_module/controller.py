from bson.json_util import dumps
from flask import Blueprint, request, jsonify,current_app
#from run import mqtt_client
import os

from apps.factory import mongo as mongoobj

# setting up blueprint
simple_blueprint= Blueprint('simple_module',__name__,url_prefix='/simple_module')


@simple_blueprint.route('/test')
def test_api():
    return jsonify({"message": "This api is working"})

@simple_blueprint.route('db/insert')
def insert():

    cities = [{"location": {'type': 'Point', 'coordinates': [10.524255, 76.213985]}, "name": "Vadakum nadhan temple"},
          {"location": {'type': 'Point', 'coordinates': [10.520847, 76.226926]}, "name": "Jublee mission hospital"},
          {"location": {'type': 'Point', 'coordinates': [10.517501, 76.207831]}, "name": "Thrissur Railway station"},
          {"location": {'type': 'Point', 'coordinates': [10.003338, 76.291527]}, "name": "Nuventure"},
          {"location": {'type': 'Point', 'coordinates': [10.003114, 76.292041]}, "name": "Flow line solutions"},
          {"location": {'type': 'Point', 'coordinates': [10.002964, 76.291943]}, "name": "Parvathy Homes"}]

    result = mongoobj.db.places.insert_many(cities)


    return jsonify({"message": "Data inserterd sucessfully "})

@simple_blueprint.route('db/place/all')
def get_places():

   
    cursor_data = mongoobj.db.places.find({})
    list_cur = list(cursor_data)
    json_data = dumps(list_cur)

    return json_data

  

@simple_blueprint.route('db/place/index')
def configure():
    mongoobj.db.places.create_index([( "location", "2dsphere" )])
    return jsonify({"message": "This api is working"})





@simple_blueprint.route('db/place/search')
def search():

    cursor_data= mongoobj.db.places.aggregate([
                                            {
                                                "$geoNear": {
                                                    "near": { "type": "Point", "coordinates": [ 10.524255, 76.213985 ] },
                                                    "spherical": True,
                                                    #"query": { "category": "Parks" },
                                                    "maxDistance": 3000,
                                                    "distanceField": "calcDistance"
                                                }
                                            }
                                            ] )

    list_cur = list(cursor_data)

    json_data = dumps(list_cur)

    return json_data