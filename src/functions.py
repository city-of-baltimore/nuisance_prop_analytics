def connect_to_sql():
    """Connects to BCIT SQL server

    Args:
        None

    Returns:
        None
    """
    import os
    import pyodbc

    CITY_USERNAME = os.environ.get('CITY_USERNAME')
    CITY_PWD = os.environ.get('CITY_PWD')
    CITY_SQL_SERVER = os.environ.get('CITY_SQL_SERVER')

    conn = pyodbc.connect('Driver={FreeTDS Driver};'
                          'Server=' + CITY_SQL_SERVER +
                          ';Database=CitiStat'
                          ';PWD=' + CITY_PWD +
                          ';UID=BALTIMORE\\' + CITY_USERNAME +
                          #';Trusted_Connection=yes'
                          ';port=1433')

    cursor = conn.cursor()
    conn.close()
    print("connection closed")