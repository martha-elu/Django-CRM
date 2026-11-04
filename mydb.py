
import mysql.connector 
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="maseng",
    port='3306',
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE Employee")

print("All Done Martha after a long trial")

cursorObject.close()
dataBase.close()