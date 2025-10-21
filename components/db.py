import pymysql

def get_connection ():
    return pymysql.connect(
    host = "localhost",
    user = "root",
    password = "#lezabesite2006#",
    database = "routify_iloilo_db",
    cursorclass = pymysql.cursors.DictCursor,
    autocommit=True
    )
    