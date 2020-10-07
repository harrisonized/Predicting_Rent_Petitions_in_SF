import psycopg2 as pg

# Functions included in this file:
# # connection_fetch_close


def connection_fetch_close(query, cred, dbname, autocommit=False):
    """opens a new connection, fetches the data, then closes the connection
    """
    connection = pg.connect(**cred, dbname=dbname) # Connect
    connection.autocommit = autocommit
    cursor = connection.cursor()
    cursor.execute(query)
    try:
        results = cursor.fetchall()
    except:
        return None
        
    connection.close()
    
    return results
