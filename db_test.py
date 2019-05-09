import pymysql

# TODO: make sure to install pymysql python package

MARVEL_ID = 1
WINNIE_DATES_DICT = {}

year = 2001
month= 1
day = 12

for i in range(1,11):
    date_string = f'{year}/{month+i-1}/{day}'
    WINNIE_DATES_DICT[i] = date_string


# We could read these in from a .properties file also
host_ip = '10.42.0.20'  # can also use hostname if available
uid = 'student'
pwd = '3210Smith'
database_to_use = 'kimtest'

# create the connection
connection = pymysql.connect(host=host_ip,
                             user=uid,
                             password=pwd,
                             db=database_to_use,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)




# try-catch-finally block to close db in case of problems

try:
    with connection.cursor() as cursor:
        # prep the insert command
        sql = 'INSERT INTO `comic_books_kim` ' + \
            '(' + \
            ' `comic_title`,' + \
            ' `comic_issue`, ' + \
            ' `comic_publisher_id`, ' + \
            ' `comic_value`, ' + \
            ' `issue_date`' + \
            ' ) ' + \
            ' VALUES (%s, %s, %s, %s, %s);'

        # execute the insert command 10 times
        for i in range(1,11):
            cursor.execute(sql, ('Winnie the Pooh', i, MARVEL_ID, 1.0, WINNIE_DATES_DICT[i]) )

    # connection is not autocommit by default.
    # So you must commit to save your changes.
    connection.commit()


    with connection.cursor() as cursor:
        # prep the sql

        # select primaryId, comic_title, comic_publisher_id for Winnie The Pooh only
        # sql = "SELECT `primary_id`, `comic_title`, `comic_publisher_id` FROM `comic_books_kim` WHERE `comic_title`=%s"
        # cursor.execute(sql, ('Winnie the Pooh'))

        # select all columns for any comic book starting with 'W'
        sql = "SELECT * FROM `comic_books_kim` where `comic_title` like 'w%' "

        # select everything from comic_books_kim table
        # sql = "SELECT * FROM `comic_books_kim` "

        # execute the query
        cursor.execute(sql)

        # get the results
        result = cursor.fetchall()

        # the result is a list of dictionaries
        print(f'Result type is : {type(result)}')
        if len(result) > 0 :
            print(f'First result object type is : {type(result[0])}')
        else:
            print('No results')
        print(result)
finally:
    connection.close()
