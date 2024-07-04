"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planets, Characters
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/users', methods=['GET'])
def get_users():

    users = User.query.all()

    if (users == ""):
        return "This user doesn't exist or is empty"
    
    users_serialized = list(map(lambda item:item.serialize(), users))

    response_body = {
        "msg": "Ok",
        "data": users_serialized
    }

    return jsonify(response_body), 200

@app.route('/user', methods=['POST'])
def create_user():

    new_user = request.json
    if (new_user["name"]=="" or new_user["surname"] == "" or new_user["email"] == "") :
        return "All field are required", 400
    
    try:
        me =  User(name=new_user["name"], surname=new_user["surname"], email=new_user["email"], sub_date=new_user["sub_date"])
        db.session.add(me)
        db.session.commit()

        response_body = {
            "msg": "Ok"
        }
        
        return jsonify(response_body), 200
    
    except:
        print("An exception occurred")
        return "AAAAAAAAAAAAA", 500


@app.route('/characters', methods=['GET'])
def handle_characters():

    characters = Characters.query.all()
    characters_serialized = list(map(lambda item:item.serialize(), characters))

    response_body = {
        "msg": "Ok",
        "data": characters_serialized
    }

    return jsonify(response_body), 200


@app.route('/characters/<int:character_id>', methods=['GET'])
def get_single_character(character_id):

    character = Characters.query.filter_by(id = character_id).first()
    character_serialized = character.serialize()

    response_body = {
        "msg": "Ok",
        "data": character_serialized
    }

    return jsonify(response_body), 200


@app.route('/characters', methods=['POST'])
def add_character():

    new_character = request.json
    character =  Characters(name=new_character["name"], hair=new_character["hair"], race=new_character["race"], years_old=new_character["years_old"], gender=new_character["gender"])
    db.session.add(character)
    db.session.commit()

    response_body = {
        "msg": "Ok"
    }

    return jsonify(response_body), 200


@app.route('/characters/<int:character_id>', methods=['DELETE'])
def delete_character(character_id):
    
    character = Characters.query.filter_by(id = character_id).first()
    db.session.delete(character)
    db.session.commit()

    response_body = {
        "msg": "Ok"
    }

    return jsonify(response_body), 200


@app.route('/planets', methods=['GET'])
def handle_planets():

    planets = Planets.query.all()
    planets_serialized = list(map(lambda item:item.serialize(), planets))

    response_body = {
        "msg": "Ok",
        "data": planets_serialized
    }

    return jsonify(response_body), 200
# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
