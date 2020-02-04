import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='mrbartucz.com',
                             user='an8520td',
                             password='Toby2020!',
                             db='an8520td_university',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

student_name = input("Please enter a student name: ")


try:
    with connection.cursor() as cursor:
        # Select all Students
        sql = "SELECT * from Students"
        sql = "SELECT * from Students where First_Name = '" + student_name + "'"
        # execute the SQL command
        cursor.execute(sql)
        
        # get the results
        for result in cursor:
            print (result)
        
      
        # If you INSERT, UPDATE or CREATE, the connection is not autocommit by default.
        # So you must commit to save your changes. 
        # connection.commit()
        

finally:
    connection.close()