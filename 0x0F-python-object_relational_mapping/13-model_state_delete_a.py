#!/usr/bin/python3
"""Script that lists all State objects from the database"""


from sys import argv
from model_state import Base, State
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
    states = session.query(State).filter(State.name.contains("a")).all()
    for state in states:
        session.delete(state)
    session.commit()
    session.close()