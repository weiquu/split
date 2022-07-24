import os
import psycopg2

class DBAccessor:
    __conn = None
    __cursor = None

    def __init__(self):
        try:
            DATABASE_URL = os.environ['DATABASE_URL']
            self.__conn = psycopg2.connect(DATABASE_URL, sslmode='require')
            self.__cursor = self.__conn.cursor()
        except(Exception, psycopg2.Error) as error:
            print("Error while opening DB accessor", error)

    def query(self, query, params):
        try:
            self.__cursor.execute(query, params)
        except(Exception, psycopg2.Error) as error:
            print("Error while querying database", error)
        return self.__cursor

    def close(self):
        if self.__conn is None:
            self.__cursor.close()
            self.__conn.close()
            print("PostgreSQL connection is closed")
            self.__conn = None
            self.__cursor = None