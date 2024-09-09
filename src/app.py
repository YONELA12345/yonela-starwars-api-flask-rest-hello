"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from sqlalchemy.exc import IntegrityError
from flask import Flask, request, jsonify, url_for,Blueprint
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import People, Planets, db, User
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

api = Blueprint('api', __name__)

CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# Add all endpoints form the API with a "api" prefix
app.register_blueprint(api, url_prefix='/api')

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)



# Simulación de usuario actual (reemplazar con autenticación real en el futuro)
CURRENT_USER_ID = 1

@app.route('/people', methods=['GET'])
def get_all_people():
    people = People.query.all()
    return jsonify([person.to_dict() for person in people])

@app.route('/people/<int:people_id>', methods=['GET'])
def get_person(people_id):
    person = People.query.get_or_404(people_id)
    return jsonify(person.to_dict())

@app.route('/planets', methods=['GET'])
def get_all_planets():
    planets = Planets.query.all()
    return jsonify([planet.to_dict() for planet in planets])

@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet = Planets.query.get_or_404(planet_id)
    return jsonify(planet.to_dict())

@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@app.route('/users/favorites', methods=['GET'])
def get_user_favorites():
    user = User.query.get_or_404(CURRENT_USER_ID)
    favorites = {
        'planets': [planet.to_dict() for planet in user.favorite_planets],
        'people': [person.to_dict() for person in user.favorite_people]
    }
    return jsonify(favorites)

@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def add_favorite_planet(planet_id):
    user = User.query.get_or_404(CURRENT_USER_ID)
    planet = Planets.query.get_or_404(planet_id)
    if planet not in user.favorite_planets:
        user.favorite_planets.append(planet)
        db.session.commit()
        return jsonify({'message': 'Planet added to favorites'}), 201
    return jsonify({'message': 'Planet already in favorites'}), 200

@app.route('/favorite/people/<int:people_id>', methods=['POST'])
def add_favorite_person(people_id):
    user = User.query.get_or_404(CURRENT_USER_ID)
    person = People.query.get_or_404(people_id)
    if person not in user.favorite_people:
        user.favorite_people.append(person)
        db.session.commit()
        return jsonify({'message': 'Person added to favorites'}), 201
    return jsonify({'message': 'Person already in favorites'}), 200

@app.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def remove_favorite_planet(planet_id):
    user = User.query.get_or_404(CURRENT_USER_ID)
    planet = Planets.query.get_or_404(planet_id)
    if planet in user.favorite_planets:
        user.favorite_planets.remove(planet)
        db.session.commit()
        return jsonify({'message': 'Planet removed from favorites'}), 200
    return jsonify({'message': 'Planet not in favorites'}), 404

@app.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def remove_favorite_person(people_id):
    user = User.query.get_or_404(CURRENT_USER_ID)
    person = People.query.get_or_404(people_id)
    if person in user.favorite_people:
        user.favorite_people.remove(person)
        db.session.commit()
        return jsonify({'message': 'Person removed from favorites'}), 200
    return jsonify({'message': 'Person not in favorites'}), 404

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
