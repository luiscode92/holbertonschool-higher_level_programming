#!/usr/bin/python3
"""Script that lists all State objects from the database"""


from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)


if __name__ == "__main__":

    user = argv[1]
    passw = argv[2]
    database = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, passw, database),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)
    rows = session.query(City, State)\
        .filter(City.state_id == State.id)\
        .order_by(City.id.asc()).all()

    for cities, states in rows:
        print("{}: ({}) {}".format(states.name, cities.id, cities.name))

    session.close()