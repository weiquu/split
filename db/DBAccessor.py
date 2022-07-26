import os
import psycopg2

class DBAccessor:
    __conn = None
    __cursor = None

    def __init__(self):
        try:
            DATABASE_URL = os.environ['DATABASE_URL']
            self.__conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        except(Exception, psycopg2.Error) as error:
            print("Error while opening DB accessor", error)

    def select(self, query, params):
        try:
            self.__cursor = self.__conn.cursor()
            self.__cursor.execute(query, params)
        except(Exception, psycopg2.Error) as error:
            print("Error while querying database", error)
        return self.__cursor

    def insert(self, query, params):
        try:
            self.__cursor = self.__conn.cursor()
            self.__cursor.execute(query, params)
            self.__conn.commit()
        except(Exception, psycopg2.Error) as error:
            print("Error while inserting into database", error)
            return False
        return True

    def insertWithReturn(self, query, params):
        id = 0
        try:
            self.__cursor = self.__conn.cursor()
            self.__cursor.execute(query, params)
            self.__conn.commit()
            id = self.__cursor.fetchone()[0]
        except(Exception, psycopg2.Error) as error:
            print("Error while inserting into database", error)
            #return False
        return id

    def update(self, query, params):
        try:
            self.__cursor = self.__conn.cursor()
            self.__cursor.execute(query, params)
            self.__conn.commit()
        except(Exception, psycopg2.Error) as error:
            print("Error while querying database", error)
            return False
        return True

    def close(self):
        if self.__conn is not None:
            self.__cursor.close()
            self.__conn.close()
            print("PostgreSQL connection is closed")
            self.__conn = None
            self.__cursor = None