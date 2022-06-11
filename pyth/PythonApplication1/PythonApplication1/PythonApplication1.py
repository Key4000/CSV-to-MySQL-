from mysql.connector import connect, Error
import csv 

csv_file = 'import.csv'

#Подключение к БД,чтение из CSV в readcsv(кортежем,tuple)

try:
    with connect(
        host = "localhost",
        user = "root",
        password = "12345qwer90",
        database = "takeacsv"
    ) as connection:
        with connection.cursor() as cursor:
            with open(csv_file, 'r' , newline = '') as csv_f:
                reader = csv.reader(csv_f)
                readcsv = map(tuple,reader)
                for row in readcsv:
                    query_insert_in_table = '''INSERT INTO testcsv2 VALUES(%s,%s)'''
                    # executemany() ??? Проблема была в нём : Not enough parameters for the SQL statement
                    cursor.execute(query_insert_in_table,row)
                    # print(type(row))
                    # print(row[0],row[1])
            cursor.close()
        connection.commit()
        connection.close()
except Error as e:
    print(e)

