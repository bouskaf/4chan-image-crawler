import pymysql

connection = pymysql.connect(host='localhost',
                             port=8890,
                             user='root',
                             password='root',
                             db='idnes',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `pokus` (`id`, `pokus`) VALUES (%s, %s)"
        cursor.execute(sql, (12345, 'pokus-pokus'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `pokus` FROM `pokus` WHERE `pokus`=%s"
        cursor.execute(sql, ('pokus-pokus',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()

