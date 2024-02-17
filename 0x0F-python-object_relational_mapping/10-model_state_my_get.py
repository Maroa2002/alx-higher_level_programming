#!/usr/bin/python3
"""
state object with name passed as argument
parameters: username, password, database name, searched state
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db = argv[3]
    searched_state = argv[4]

    engine = create_engine(f'mysql+mysqldb://{username}:{password}\
                           @localhost:3306/{db}')
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == searched_state).first()
    if state:
        print(state.id)
    else:
        print('Nothing')

    session.close()
