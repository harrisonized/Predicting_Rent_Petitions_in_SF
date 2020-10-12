import os
from configparser import ConfigParser
from .encryption_tools import decrypt_message
import psycopg2 as pg

INI_KEY = os.getenv('INI_KEY')  # Make sure this is in your ~/.bashrc


# Functions included in this file:
# # postgres_session
# # connection_fetch_close


def postgres_connection(database=None,
                        section='postgres', cfg_path='cred/config.ini'):
    """Given an INI file with a ['postgres'] section
    Returns the sqlalchemy connection args 

    Make sure the config.ini file exists in your project
    """
    cfg = ConfigParser()
    cfg.read(cfg_path)

    username, password, host, port = (
        decrypt_message(cfg.get(section, key), INI_KEY)
        for key in ['username', 'password', 'host', 'port']
    )

    if database:
        connection_uri = f'postgres://{username}:{password}@{host}:{port}/{database}'
    else:
        connection_uri = f'postgres://{username}:{password}@{host}:{port}'

    return connection_uri


def postgres_connect_fetch_close(query, connection_uri, dbname=None):
    """Opens a new connection, fetches the data, then closes the connection
    Provide the connection_uri returned by postgres_connection
    Use dbname to change the database
    """
    connection = pg.connect(dsn=connection_uri, dbname=dbname) # Connect
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    connection.close()
    
    return results
