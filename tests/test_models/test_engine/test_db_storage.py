#!/usr/bin/python3
""" Module for testing db storage"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models import storage
import os
import MySQLdb

hbnb_mysql_db = os.getenv('HBNB_MYSQL_DB')
hbnb_mysql_user = os.getenv("HBNB_MYSQL_USER")
hbnb_mysql_pwd = os.getenv("HBNB_MYSQL_PWD")
hbnb_mysql_host = os.getenv("HBNB_MYSQL_HOST")
hbnb_mysql_db = os.getenv("HBNB_MYSQL_DB")
hbnb_env = os.getenv("HBNB_ENV")


class test_DBStorage(unittest.TestCase):
    """ Class to test the db storage method """

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_created_at(self):
        """Checks the created_at attribute of a new object"""
        new = BaseModel()
        self.assertTrue(type(new.created_at) is datetime)

    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    
    # def test_base_model_instantiation(self):
    #     """ File is not created on BaseModel save """
    #     new = BaseModel()
    #     """aqui toca mirar si la db existe"""

    #     db = MySQLdb.connect(
    #         host="localhost",
    #         port=3306,
    #         user=hbnb_mysql_user,
    #         password=hbnb_mysql_pwd,
    #         database=hbnb_mysql_db)

    #     cur = db.cursor()
    #     query = "SHOW DATABASES LIKE '{}'".format(hbnb_mysql_db)
    #     cur.execute(query)
    #     rows = cur.fetchall()
    #     self.assertEqual(rows, None)
    

    def test_engine_exists(self):
        """checks if engine exists"""
        new = BaseModel()
        self.assertTrue(storage._DBStorage__engine != None)

    def test_env(self):
        """checks if the env variable is test"""
        self.assertNotEqual(hbnb_env, "test")