import time
import random
import logging
from argparse import ArgumentParser, RawTextHelpFormatter

import psycopg2
import psycopg2.extras
from psycopg2.errors import SerializationFailure

#loading password
import json
with open("secret.json") as f:
    secret = json.load(f)

def checkConnection():
    #connection with database
    try:
        conn = psycopg2.connect(user=secret['DB_USER'],
                                  password=secret['DB_PASS'],
                                  host=secret['DB_HOST'],
                                  port=secret['DB_PORT'],
                                  database=secret['DB_NAME'])
        print("Connected to SMU DB")
        return conn

    except (Exception, psycopg2.Error) as error:
        print("Failed to complete request", error)
        return False

def closeConnection(conn):
    #closing database connection.
    if conn:
        conn.close()
        print("PostgreSQL connection is closed")

         
def createTableSubscribers(sid):
    conn = checkConnection()
    cur = conn.cursor()
    cur.execute('''CREATE TABLE _''' + sid + '''_subscribers(
        id BIGSERIAL NOT NULL PRIMARY KEY, 
        email VARCHAR(150) NOT NULL);''')
    conn.commit()
    closeConnection(conn)

def createTableTemplates(sid):
    conn = checkConnection()
    cur = conn.cursor()
    cur.execute('''CREATE TABLE _''' + sid + '''_templates(
        id BIGSERIAL NOT NULL PRIMARY KEY, 
        name VARCHAR(50) NOT NULL, 
        link VARCHAR(50) NOT NULL);''')
    conn.commit()
    closeConnection(conn)

# sid = server id
# createTableSubscribers() #creates a table for subscribers with name _sid_subscribers
# createTableTemplates() #creates a table for templates with name _sid_templates
# checkConnection() # returns cursor object if connected and False if connection fails
# closeConnection() # when all operations over :D   

#for testing
if __name__ == '__main__':
    createTableTemplates("53")
    createTableSubscribers("53")