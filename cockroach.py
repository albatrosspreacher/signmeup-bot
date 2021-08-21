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

#connection with database
try:
    conn = psycopg2.connect(user=secret['DB_USER'],
                                  password=secret['DB_PASS'],
                                  host=secret['DB_HOST'],
                                  port=secret['DB_PORT'],
                                  database=secret['DB_NAME'])
    cur = conn.cursor()

except (Exception, psycopg2.Error) as error:
    print("Failed to complete request", error)

#closing database connection.
finally:
    if conn:
        cur.close()
        conn.close()
        print("PostgreSQL connection is closed")


