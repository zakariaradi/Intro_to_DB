import mysql.connector

try:
    # CONNECT TO MYSQL SERVER (NO DATABASE SPECIFIED)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",          # غيّر إذا لزم الأمر
        password="PASSWORD"   # ضع كلمة المرور الصحيحة
    )

    cursor = connection.cursor()

    # CREATE DATABASE IF IT DOES NOT EXIST
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print("Error while connecting to MySQL:", err)

finally:
    # CLOSE CURSOR AND CONNECTION
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
