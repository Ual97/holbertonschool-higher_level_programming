#!/usr/bin/python3

"""script that lists all states with a name starting
 with N from the databse hbtn_0e_0_usa."""

from itertools import count
import MySQLdb
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    arizona = session.query(State).filter_by(id=2).first()
    arizona.name = "New Mexico"
    session.commit()
    session.close()
