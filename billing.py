import mysql.connector

mydb = mysql.connector.connect(
            host="192.46.225.247",
            user="joeysabusido",
            password="Genesis@11",
            database="ldglobal",
            auth_plugin='mysql_native_password')
cursor = mydb.cursor()
