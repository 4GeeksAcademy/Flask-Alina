from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    surname = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    sub_date = db.Column(db.String(250), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            "sub_date" : self.sub_date
        }

class Planets(db.Model):
    __tablename__ = 'Planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String(250),nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "planets_name": self.planet_name
        }
    
class Characters(db.Model):
    __tablename__ = 'Characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250),nullable=False)
    hair = db.Column(db.String(250),nullable=False)
    race = db.Column(db.String(250),nullable=False)
    years_old = db.Column(db.Integer,nullable=False)
    gender = db.Column(db.String(250),nullable=False)
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "hair": self.hair,
            "race": self.race,
            "years_old": self.years_old,
            "gender": self.gender,
        }

# class Fav_Characters():
#     __tablename__ = 'Fav_Characters'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('User.id'),nullable=False)
#     character_id = Column(Integer, ForeignKey('Characters.id'),nullable=False)

# class Vehicles():
#     __tablename__ = 'Vehicles'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     model = Column(String(250),nullable=True)
#     vehicle_name = Column(String(250),nullable=False)

# class Fav_Vehicles():
#     __tablename__ = 'Fav_Vehicles'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('User.id'),nullable=False)
#     vehicle_id = Column(Integer, ForeignKey('Vehicles.id'),nullable=False)


# class Fav_Planets():
#     __tablename__ = 'Fav_Planets'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('User.id'),nullable=False)
#     planet_id = Column(Integer, ForeignKey('Planets.id'),nullable=False)


#    def to_dict(self):
 #       return {}
