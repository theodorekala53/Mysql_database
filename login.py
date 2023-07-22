import tkinter as tk
import mysql.connector
import os # wichtig für  export DB_PASSWORD="IhrPasswortHier"

# verrbindung zur Datenbank herstellen
db_connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = os.environ.get("DB_PASSWORD"), # export DB_PASSWORD="IhrPasswortHier" so legt den pass fest
    database = "user_db"
)
try:
    if db_connection.is_connected():
        print("Verbindung erfolgreich")
        db_connection.close()

except mysql.connector.Error as error:
    print("Fehler bei der Verbindung", error)
    
    
def login():
    db_connection._open_connection()
    benutzername = username_entry.get()
    passwort = password_entry.get()
    
    # überprüfen, ob die Daten bereit in der Db vorhandelt sind
    cursor = db_connection.cursor()
    query = "SELECT * FROM benutzer WHERE benutzername = %s AND passwort = %s"
    values = (benutzername, passwort)
    cursor.execute(query, values)
    exist_user = cursor.fetchall()
    
    if exist_user:
        print("login erfolgreich")
    else:
        print("login nicht erfolgreich")
    

# Tkinter-Fenster erstellen
root = tk.Tk()
root.title("Login-Fenster")
root.geometry("500x400")

# Benutzernamen-Label und Eingabefeld
username_label = tk.Label(root, text="Benutzername:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Passwort-Label und Eingabefeld
password_label = tk.Label(root, text="Passwort:")
password_label.pack()
password_entry = tk.Entry(root, show="*")  # Zeigt die Passworteingabe als Sternchen an
password_entry.pack()

# Login-Schaltfläche
login_button = tk.Button(root, text="Login", command=login) # TODO: login
login_button.pack()

# Tkinter starten
root.mainloop()