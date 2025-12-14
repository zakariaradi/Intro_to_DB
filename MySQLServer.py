import mysql.connector
from mysql.connector import Error

try:
    # CONNECT TO MYSQL SERVER (NO DATABASE SPECIFIED)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",          # غيّر إذا لزم الأمر
        password="PASSWORD"   # ضع كلمة المرور الصحيحة
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # CREATE DATABASE IF IT DOES NOT EXIST
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print("Error while connecting to MySQL:", e)

finally:
    # CLOSE CURSOR AND CONNECTION
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
