#!/usr/bin/python3
"""
all City objects
parameters: username, password, database name
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db = argv[3]

    engine = create_engine(f'mysql+mysqldb://{username}:{password}\
                           @localhost:3306/{db}')
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(State.name, City.id, City.name).filter(
             City.state_id == State.id).order_by(City.id).all()
    for city in cities:
        print(f'{city[0]}: ({city[1]}) {city[2]}')

    session.close()
