#!/usr/bin/python3
"""
adding the state Louisiana
parameters: username, password, database name
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db = argv[3]

    engine = create_engine(f'mysql+mysqldb://{username}:{password}\
                           @localhost:3306/{db}')
    Session = sessionmaker(bind=engine)
    session = Session()

    Louisiana = State(name='Louisiana')
    session.add(Louisiana)
    session.commit()
    print(Louisiana.id)

    session.close()
