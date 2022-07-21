import pymysql

# Open database connection
db = pymysql.connect("localhost","root","","logistics")

# prepare a cursor object using cursor() method
cursor = db.cursor()

#sql_query = """ insert into users(firstname, lastname, email, password) values('Ibrahim','Aminu','aminu@gmail.com','1234') """
sql = "SELECT `email`, `firstname` FROM `users` WHERE `email`=%s"

try :
    cursor.execute(sql,('hello@di-hub.com'))
    data = cursor.fetchone()
    db.commit()
    print("The user exit in the database:{}".format(data))
except Exception as e:
    print("Exception:",e)

db.close()