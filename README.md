# Jeffrey Shen Sipher Project

_Python interactive command line interface for PostgreSQL database with randomized key/value pairs_



# Setup

## Dependencies
- [Python3](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [psycopg2](https://www.psycopg.org/docs/install.html)

## Steps
1. Download [PostgreSQL](https://www.postgresql.org/download/) [tested on v13.2/MacOS]
    - Go through set up process for your machine, choosing default settings
2. Install `psycopg2` for interacting with PostgreSQL in Python
    - Using pip: `pip install psycopg2-binary` 
3. Open PostgreSQL command line
    - For MacOS: open `SQL Shell (pqsql).app`, other setup methods may differ
    - When prompted, press Enter to set defaults for Server, Database, Port, Username
    - Set password as `password` (temporary for this test app. Feel free to change but will need to update `password` variable in `db.py`)
        ```
        Server [localhost]: 
        Database [postgres]: 
        Port [5432]: 
        Username [postgres]: 
        Password for user postgres: password
        ```




# Testing/Running

Simply run `python3 client.py` to start up the interactive command line interface.

Here you can choose to either:
1. `add`: Insert a new key-value pair (saved as randomized hashes) into the table
2. `view`: See the contents of the table in the database and number of numbers in the table
3. `exit`: Quit the interactive command line interface


# File Structure
`db.py` 

This file contains code for interacting with PostgreSQL database. It contains methods for connecting to the database, adding a key-value pair, and viewing the contents of the table. Look here to update database connection settings, or change entries to add to the database. 

`client.py` 

This Python file contains code to start up the interactive command line interface. It contains the code to set up the interface and respond to specific commands, directing it to methods in `db.py`.

