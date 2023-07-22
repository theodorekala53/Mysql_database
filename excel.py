import tkinter as tk
import mysql.connector

try:
    # Verbindung zur MySQL-Datenbank herstellen
    db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ykm1953.",
    database="user_db"
    )
    
    if db_connection.is_connected():
        print("Verbindung zu MysQl erfolgreich ergestellt")
        db_connection.close()
except mysql.connector.Error as error:
    print("Fehler bei der Verbindung zu der Datenbank", error)