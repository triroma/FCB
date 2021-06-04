import pymysql.cursors


def getConnection():
    connection = pymysql.connect(host="127.0.0.1",
                                 user="root",
                                 password="269973514",
                                 db="users",
                                 charset='utf8mb4',
                                 port=3307,
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection
