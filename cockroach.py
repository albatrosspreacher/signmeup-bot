from dotenv import load_dotenv
import os, time, random, logging, psycopg2, psycopg2.extras
from argparse import ArgumentParser, RawTextHelpFormatter
from psycopg2.errors import SerializationFailure
load_dotenv()

#loading password
import json
with open("secret.json") as f:
    secret = json.load(f)

# with secrets.json
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

""" # with env file
def checkConnection():
    #connection with database
    try:
        conn = psycopg2.connect(user=os.getenv('DB_USER'),
                                    password=os.getenv('DB_PASS'),
                                    host=os.getenv('DB_HOST'),
                                    port=os.getenv('DB_PORT'),
                                    database=os.getenv('DB_NAME'))
        cur = conn.cursor()
        print("Connected to SMU DB")
        return conn

    except (Exception, psycopg2.Error) as error:
        print("Failed to complete request", error)
        return False """

def closeConnection():
    conn = checkConnection()
    cur = conn.cursor()
    #closing database connection.
    if conn:
        cur.close()
        conn.close()
        print("PostgreSQL connection is closed")

         
def createTableSubscribers(sid):
    conn = checkConnection()
    cur = conn.cursor()
    cur.execute('''CREATE TABLE _''' + str(sid) + '''_subscribers(
        id BIGSERIAL NOT NULL PRIMARY KEY, 
        email VARCHAR(150) NOT NULL);''')
    conn.commit()
    closeConnection()

def createTableTemplates(sid):
    conn = checkConnection()
    cur = conn.cursor()
    cur.execute('''CREATE TABLE _''' + str(sid) + '''_templates(
        id BIGSERIAL NOT NULL PRIMARY KEY, 
        name VARCHAR(50) NOT NULL, 
        link VARCHAR(50) NOT NULL);''')
    conn.commit()
    closeConnection()

def readDataTemplates(sid):
    conn = checkConnection()
    cur = conn.cursor()
    tableName = "_" + str(sid) + "_templates" 
    cur.execute("SELECT * FROM " + tableName)
    cur.execute("SELECT COUNT (*) FROM " + tableName)
    count = cur.fetchone()
    cur.execute("SELECT * FROM " + tableName)
    for x in cur.fetchall():
        print (x)
        return x
    conn.commit()
    closeConnection()

def readDataSubscribers(sid):
    conn = checkConnection()
    cur = conn.cursor()
    tableName = "_" + str(sid) + "_subscribers" 
    cur.execute("SELECT * FROM " + tableName)
    cur.execute("SELECT COUNT (*) FROM " + tableName)
    count = cur.fetchone()
    cur.execute("SELECT * FROM " + tableName)
    for x in cur.fetchall():
        print (x)
        return x
    conn.commit()
    closeConnection()

#for testing
if __name__ == '__main__':
    checkConnection()
    closeConnection()
    createTableTemplates(50)
    createTableSubscribers(50)
    readDataTemplates(52)
    readDataSubscribers(52)