#!/usr/bin/python3
"""Script that lists all State objects from the database"""


from sys import argv
from relationship_state import Base, State
from relationship_city import City
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
    new_state = State(name="California")
    new_city = City(name="San Francisco")
    new_state.cities.append(new_city)
    session.add(new_state)
    session.commit()
    session.close()