import psycopg2
import uuid 

hostname = 'localhost'
username = 'postgres'
password = 'password'
database = 'postgres'

table_var = "KVPAIRS"
key_var = "KEY"
value_var = "VALUE"


def connect():
    '''
    Returns connection to database using the given global variables for hostname, username, password, and database. 
    '''
    conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
    cur = conn.cursor()
    cur.execute(f'''CREATE TABLE IF NOT EXISTS {table_var}
      ({key_var} TEXT PRIMARY KEY     NOT NULL,
      {value_var}           TEXT    NOT NULL
      );''')
    conn.commit()
    return conn


def print_table():
    '''
    Connects to database and prints out key value pairs in table as well as total rows.
    '''
    conn = connect()
    cur = conn.cursor()
    cur.execute(f'''SELECT {key_var}, {value_var} FROM {table_var}''')
    rows = cur.fetchall()
    for row in rows:
        if len(row) >= 2:
            print(row[0], ":", row[1])
    print("Total Entries:", len(rows))
    conn.close()


def add_random_kv():
    '''
    Connects to database and adds a randomized key value pair to the db. Key and value are random hashes. Also retrieves total number of entries to obtain times updated.
    '''
    conn = connect()
    cur = conn.cursor()
    record = (str(uuid.uuid4().hex), str(uuid.uuid4().hex))
    print(f"Adding {key_var}={record[0]}, {value_var}={record[1]} into database...")
    cur.execute(f'''INSERT INTO {table_var} ({key_var}, {value_var}) VALUES (%s, %s)''', record)
    conn.commit()
    count = cur.rowcount
    print(count, "Record inserted successfully into Table")

    cur.execute(f'''SELECT {key_var}, {value_var} FROM {table_var}''')
    rows = cur.fetchall()
    print(f"Database has been updated a total of {len(rows)} times")
    conn.close()


def main():
    add_random_kv()
