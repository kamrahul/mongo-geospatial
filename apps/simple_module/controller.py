from bson.json_util import dumps
from flask import Blueprint, request, jsonify,current_app
import os

from apps.factory import mongo as mongoobj

# setting up blueprint
simple_blueprint= Blueprint('simple_module',__name__,url_prefix='/simple_module')


@simple_blueprint.route('/test')
def test_api():
    return jsonify({"message": "This api is working"})



@simple_blueprint.route("image/uploads/<path:filename>")
def get_image_api(filename):
    response = mongoobj.send_file(filename)
    print(response.mimetype)


@simple_blueprint.route("image/upload/<path:filename>", methods=["POST"])
def save_upload(filename):
    mongoobj.save_file(filename, request.files["file"])
    return {"test":"ok"}
    #return redirect(url_for("get_upload", filename=filename))


