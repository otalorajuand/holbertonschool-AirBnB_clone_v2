#!/usr/bin/python3
"""
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
import os
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel, Base


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """init method"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.getenv("HBNB_MYSQL_USER"),
            os.getenv("HBNB_MYSQL_PWD"),
            os.getenv("HBNB_MYSQL_HOST"),
            os.getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session all objects depending of the class name"""
        dic_query = {}
        classes = [User, State, City, Amenity, Place, Review]

        # self.create_session()

        if cls:
            objs = self.__session.query(cls).all()

            for obj in objs:
                dic_query[type(obj).__name__+"."+obj.id] = obj # CORREGIR
        else:
            for elem in classes:
                objs = self.__session.query(elem).all()
                for obj in objs:
                    dic_query[type(obj).__name__+"."+obj.id] = obj

        return dic_query

    def new(self, obj):
        """adds the object to the current database session"""
        # self.create_session()

        self.__session.add(obj)
        # self.__session.commit()
        # self.__session.close()

    def save(self):
        """commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes from the current database session obj if not None"""
        # self.create_session()
        if obj is not None: # ...
            self.__session.delete(obj)
        # self.__session.commit()
        # self.__session.close()

    def reload(self):
        """creates all tables in the database """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()


    # def create_session(self):
    #     """creates a session connection"""
    #     Session = sessionmaker(bind=self.__engine)
    #     conn = self.__engine.connect()
    #     self.__session = Session(bind=conn)
