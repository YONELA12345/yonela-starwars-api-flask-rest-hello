from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float, Table
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask-SQLAlchemy
db = SQLAlchemy()

# Association tables for many-to-many relationships
films_people_association = db.Table(
    'films_people', db.metadata,
    Column('film_id', Integer, ForeignKey('films.id')),
    Column('person_id', Integer, ForeignKey('people.id'))
)

films_starships_association = db.Table(
    'films_starships', db.metadata,
    Column('film_id', Integer, ForeignKey('films.id')),
    Column('starship_id', Integer, ForeignKey('starships.id'))
)

films_vehicles_association = db.Table(
    'films_vehicles', db.metadata,
    Column('film_id', Integer, ForeignKey('films.id')),
    Column('vehicle_id', Integer, ForeignKey('vehicles.id'))
)

films_species_association = db.Table(
    'films_species', db.metadata,
    Column('film_id', Integer, ForeignKey('films.id')),
    Column('species_id', Integer, ForeignKey('species.id'))
)

films_planets_association = db.Table(
    'films_planets', db.metadata,
    Column('film_id', Integer, ForeignKey('films.id')),
    Column('planet_id', Integer, ForeignKey('planets.id'))
)

people_species_association = db.Table(
    'people_species', db.metadata,
    Column('person_id', Integer, ForeignKey('people.id')),
    Column('species_id', Integer, ForeignKey('species.id'))
)

# New association table for people and starships
people_starships_association = db.Table(
    'people_starships', db.metadata,
    Column('person_id', Integer, ForeignKey('people.id')),
    Column('starship_id', Integer, ForeignKey('starships.id'))
)

# New association table for people and vehicles
people_vehicles_association = db.Table(
    'people_vehicles', db.metadata,
    Column('person_id', Integer, ForeignKey('people.id')),
    Column('vehicle_id', Integer, ForeignKey('vehicles.id'))
)

# Association tables for user favorites
user_favorite_planets = db.Table(
    'user_favorite_planets', db.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('planet_id', Integer, ForeignKey('planets.id'))
)

user_favorite_species = db.Table(
    'user_favorite_species', db.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('species_id', Integer, ForeignKey('species.id'))
)

user_favorite_vehicles = db.Table(
    'user_favorite_vehicles', db.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('vehicle_id', Integer, ForeignKey('vehicles.id'))
)

user_favorite_starships = db.Table(
    'user_favorite_starships', db.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('starship_id', Integer, ForeignKey('starships.id'))
)

user_favorite_films = db.Table(
    'user_favorite_films', db.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('film_id', Integer, ForeignKey('films.id'))
)

# People Model
class People(db.Model):
    __tablename__ = 'people'
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(250), nullable=False)
    birth_year = db.Column(String(10))
    eye_color = db.Column(String(50))
    gender = db.Column(String(10))
    hair_color = db.Column(String(50))
    height = db.Column(Integer)
    mass = db.Column(Float)
    skin_color = db.Column(String(50))
    homeworld_id = db.Column(Integer, ForeignKey('planets.id'))
    created = db.Column(DateTime)
    edited = db.Column(DateTime)
    url = db.Column(String(250))

    films = db.relationship("Films", secondary=films_people_association, back_populates="characters")
    species = db.relationship("Species", secondary=people_species_association, back_populates="people")
    starships = db.relationship("Starships", secondary=people_starships_association, back_populates="pilots")
    vehicles = db.relationship("Vehicles", secondary=people_vehicles_association, back_populates="pilots")
    homeworld = db.relationship("Planets", back_populates="residents")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'birth_year': self.birth_year,
            'eye_color': self.eye_color,
            'gender': self.gender,
            'hair_color': self.hair_color,
            'height': self.height,
            'mass': self.mass,
            'skin_color': self.skin_color,
            'homeworld_id': self.homeworld_id,
            'created': self.created,
            'edited': self.edited,
            'url': self.url,
            'films': [film.to_dict() for film in self.films],
            'species': [specie.to_dict() for specie in self.species],
            'starships': [starship.to_dict() for starship in self.starships],
            'vehicles': [vehicle.to_dict() for vehicle in self.vehicles],
            'homeworld': self.homeworld.to_dict() if self.homeworld else None
        }


# Films Model
class Films(db.Model):
    __tablename__ = 'films'
    id = db.Column(Integer, primary_key=True)
    title = db.Column(String(250), nullable=False)
    episode_id = db.Column(Integer)
    opening_crawl = db.Column(String(500))
    director = db.Column(String(100))
    producer = db.Column(String(100))
    release_date = db.Column(DateTime)
    created = db.Column(DateTime)
    edited = db.Column(DateTime)
    url = db.Column(String(250))

    characters = db.relationship("People", secondary=films_people_association, back_populates="films")
    planets = db.relationship("Planets", secondary=films_planets_association, back_populates="films")
    starships = db.relationship("Starships", secondary=films_starships_association, back_populates="films")
    vehicles = db.relationship("Vehicles", secondary=films_vehicles_association, back_populates="films")
    species = db.relationship("Species", secondary=films_species_association, back_populates="films")

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'episode_id': self.episode_id,
            'opening_crawl': self.opening_crawl,
            'director': self.director,
            'producer': self.producer,
            'release_date': self.release_date,
            'created': self.created,
            'edited': self.edited,
            'url': self.url,
            'characters': [character.to_dict() for character in self.characters],
            'planets': [planet.to_dict() for planet in self.planets],
            'starships': [starship.to_dict() for starship in self.starships],
            'vehicles': [vehicle.to_dict() for vehicle in self.vehicles],
            'species': [specie.to_dict() for specie in self.species]
        }


# Starships Model
class Starships(db.Model):
    __tablename__ = 'starships'
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(250), nullable=False)
    model = db.Column(String(250))
    manufacturer = db.Column(String(250))
    cost_in_credits = db.Column(String(50))
    length = db.Column(String(50))
    max_atmosphering_speed = db.Column(String(50))
    crew = db.Column(Integer)
    passengers = db.Column(Integer)
    cargo_capacity = db.Column(String(50))
    consumables = db.Column(String(50))
    hyperdrive_rating = db.Column(String(50))
    MGLT = db.Column(String(50))
    starship_class = db.Column(String(100))
    created = db.Column(DateTime)
    edited = db.Column(DateTime)
    url = db.Column(String(250))

    films = db.relationship("Films", secondary=films_starships_association, back_populates="starships")
    pilots = db.relationship("People", secondary=people_starships_association, back_populates="starships")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'model': self.model,
            'manufacturer': self.manufacturer,
            'cost_in_credits': self.cost_in_credits,
            'length': self.length,
            'max_atmosphering_speed': self.max_atmosphering_speed,
            'crew': self.crew,
            'passengers': self.passengers,
            'cargo_capacity': self.cargo_capacity,
            'consumables': self.consumables,
            'hyperdrive_rating': self.hyperdrive_rating,
            'MGLT': self.MGLT,
            'starship_class': self.starship_class,
            'created': self.created,
            'edited': self.edited,
            'url': self.url,
            'films': [film.to_dict() for film in self.films],
            'pilots': [pilot.to_dict() for pilot in self.pilots]
        }


# Vehicles Model
class Vehicles(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(250), nullable=False)
    model = db.Column(String(250))
    manufacturer = db.Column(String(250))
    cost_in_credits = db.Column(String(50))
    length = db.Column(String(50))
    max_atmosphering_speed = db.Column(String(50))
    crew = db.Column(Integer)
    passengers = db.Column(Integer)
    cargo_capacity = db.Column(String(50))
    consumables = db.Column(String(50))
    vehicle_class = db.Column(String(100))
    created = db.Column(DateTime)
    edited = db.Column(DateTime)
    url = db.Column(String(250))

    films = db.relationship("Films", secondary=films_vehicles_association, back_populates="vehicles")
    pilots = db.relationship("People", secondary=people_vehicles_association, back_populates="vehicles")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'model': self.model,
            'manufacturer': self.manufacturer,
            'cost_in_credits': self.cost_in_credits,
            'length': self.length,
            'max_atmosphering_speed': self.max_atmosphering_speed,
            'crew': self.crew,
            'passengers': self.passengers,
            'cargo_capacity': self.cargo_capacity,
            'consumables': self.consumables,
            'vehicle_class': self.vehicle_class,
            'created': self.created,
            'edited': self.edited,
            'url': self.url,
            'films': [film.to_dict() for film in self.films],
            'pilots': [pilot.to_dict() for pilot in self.pilots]
        }



# Species Model
class Species(db.Model):
    __tablename__ = 'species'
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(250), nullable=False)
    classification = db.Column(String(100))
    designation = db.Column(String(50))
    average_height = db.Column(String(50))
    skin_colors = db.Column(String(100))
    hair_colors = db.Column(String(100))
    eye_colors = db.Column(String(100))
    average_lifespan = db.Column(String(50))
    homeworld_id = db.Column(Integer, ForeignKey('planets.id'))
    language = db.Column(String(100))
    created = db.Column(DateTime)
    edited = db.Column(DateTime)
    url = db.Column(String(250))

    people = db.relationship("People", secondary=people_species_association, back_populates="species")
    films = db.relationship("Films", secondary=films_species_association, back_populates="species")
    homeworld = db.relationship("Planets", back_populates="native_species")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'classification': self.classification,
            'designation': self.designation,
            'average_height': self.average_height,
            'skin_colors': self.skin_colors,
            'hair_colors': self.hair_colors,
            'eye_colors': self.eye_colors,
            'average_lifespan': self.average_lifespan,
            'homeworld_id': self.homeworld_id,
            'language': self.language,
            'created': self.created,
            'edited': self.edited,
            'url': self.url,
            'people': [person.to_dict() for person in self.people],
            'films': [film.to_dict() for film in self.films],
            'homeworld': self.homeworld.to_dict() if self.homeworld else None
        }



# Planets Model
class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(250), nullable=False)
    climate = db.Column(String(50))
    diameter = db.Column(String(50))
    gravity = db.Column(String(50))
    orbital_period = db.Column(String(50))
    population = db.Column(String(50))
    rotation_period = db.Column(String(50))
    surface_water = db.Column(String(50))
    terrain = db.Column(String(100))
    created = db.Column(DateTime)
    edited = db.Column(DateTime)
    url = db.Column(String(250))

    films = db.relationship("Films", secondary=films_planets_association, back_populates="planets")
    residents = db.relationship("People", back_populates="homeworld")
    native_species = db.relationship("Species", back_populates="homeworld")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'climate': self.climate,
            'diameter': self.diameter,
            'gravity': self.gravity,
            'orbital_period': self.orbital_period,
            'population': self.population,
            'rotation_period': self.rotation_period,
            'surface_water': self.surface_water,
            'terrain': self.terrain,
            'created': self.created,
            'edited': self.edited,
            'url': self.url,
            'films': [film.to_dict() for film in self.films],
            'residents': [resident.to_dict() for resident in self.residents],
            'native_species': [specie.to_dict() for specie in self.native_species]
        }



# User Model
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(Integer, primary_key=True)
    username = db.Column(String(50), nullable=False, unique=True)
    email = db.Column(String(100), nullable=False, unique=True)
    password = db.Column(String(100), nullable=False)
    created_at = db.Column(DateTime)

    # Relationships with the favorites
    favorite_planets = db.relationship('Planets', secondary=user_favorite_planets, backref='favorited_by_users')
    favorite_species = db.relationship('Species', secondary=user_favorite_species, backref='favorited_by_users')
    favorite_vehicles = db.relationship('Vehicles', secondary=user_favorite_vehicles, backref='favorited_by_users')
    favorite_starships = db.relationship('Starships', secondary=user_favorite_starships, backref='favorited_by_users')
    favorite_films = db.relationship('Films', secondary=user_favorite_films, backref='favorited_by_users')

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at,
            'favorite_planets': [planet.to_dict() for planet in self.favorite_planets],
            'favorite_species': [specie.to_dict() for specie in self.favorite_species],
            'favorite_vehicles': [vehicle.to_dict() for vehicle in self.favorite_vehicles],
            'favorite_starships': [starship.to_dict() for starship in self.favorite_starships],
            'favorite_films': [film.to_dict() for film in self.favorite_films]
        }    