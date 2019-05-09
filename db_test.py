import pymysql

# sqlalchemy?

MARVEL_ID = 1

WINNIE_DATES_DICT = {}

year = 2001
month= 1
day = 12

for i in range(1,11):
    date_string = f'{year}/{month+i-1}/{day}'
    WINNIE_DATES_DICT[i] = date_string


connection = pymysql.connect(host='10.42.0.20',
                             user='student',
                             password='3210Smith',
                             db='kimtest',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


# try-catch-finally block to close db in case of problems



try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = 'INSERT INTO `comic_books_kim` ' + \
            '(' + \
            ' `comic_title`,' + \
            ' `comic_issue`, ' + \
            ' `comic_publisher_id`, ' + \
            ' `comic_value`, ' + \
            ' `issue_date`' + \
            ' ) ' + \
            ' VALUES (%s, %s, %s, %s, %s);'

        for i in range(1,11):
            cursor.execute(sql, ('Winnie the Pooh', i, MARVEL_ID, 1.0, WINNIE_DATES_DICT[i]) )

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `primary_id`, `comic_title`, `comic_publisher_id` FROM `comic_books_kim` WHERE `comic_title`=%s"
        cursor.execute(sql, ('Winnie the Pooh'))
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()
