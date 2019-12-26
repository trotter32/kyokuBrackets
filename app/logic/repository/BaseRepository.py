import sqlite3
from functools import wraps

import mysql.connector

from app.logic.repository.ConnectionDecorator import open_close_connection


class BaseRepository:
    def __init__(self):
        self.conn = None

    def execute_statement(self, statement):
        cursor = self.get_cursor()
        cursor.execute(statement)
        self.close_connection()
        return cursor

    def get_cursor(self):
        self.conn =sqlite3.connect('SQLite_Python.db')
        print("Database created and Successfully Connected to SQLite")
        #mysql.connector.connect(
            #host="localhost",
            #user="yourusername",
            #passwd="yourpassword"
            #host="127.0.0.1",
            #port="3306",
            #user='root',
            #password="mislnipr",
            #auth_plugin='mysql_native_password'
            #)
        return self.conn.cursor()


    def close_connection(self):
        self.conn.cursor().close()
        self.conn.close()

    def create_db(self):
        self.execute_statement("""
            CREATE DATABASE IF NOT EXISTS db_main;
            USE db_main;
        """)

    def select_all(self, table_name):
        cursor = self.get_cursor()
        cursor.execute("SELECT * FROM " + table_name)
        self.close_connection()
        return cursor.fetchall()

    def select_by_id(self, id_, table_name):

        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM " + table_name + " WHERE id = " + id_)
        return cursor.fetchone()

    def add(self, object):
        cursor = self.conn.cursor()
        cursor.execute(
            'INSERT INTO ' + object.table_name + ' (' + object.get_table_variable_names() + ') VALUES (' +
            object.get_table_variables() + ');')
        return cursor.fetchone()


class TestRepository(BaseRepository):
    def __init__(self):
        super().__init__()
