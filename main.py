import tkinter as tk
import mysql.connector

# Verbindung zur MySQL-Datenbank herstellen
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ykm1953.",
    database="user_db"
)


# Funktion zum Einfügen der Benutzerdaten in die Datenbank
def insert_user():
    benutzername = entry_benutzername.get()
    passwort = entry_passwort.get()
    email = entry_email.get()
    
    # Überprüfen, ob der Benutzer bereits in der Datenbank existiert
    cursor = db_connection.cursor()
    query = "SELECT * FROM benutzer WHERE benutzername = %s OR email = %s"
    values = (benutzername, email)
    cursor.execute(query, values)
    existing_user = cursor.fetchone()
    
    if existing_user:
        print("Username schon in der Datenbank")
    else:
        sql_query = "INSERT INTO benutzer (benutzername, passwort, email) VALUES (%s, %s, %s)"
        insert_values = (benutzername, passwort, email)
        
        cursor.execute(sql_query, insert_values)
        db_connection.commit()
        cursor.close()
        
        print("Benutzer erfolgreich hinzugefügt")




    print("Benutzerdaten erfolgreich hinzugefügt!")

# Tkinter-Fenster erstellen
root = tk.Tk()
root.title("Benutzerdaten eingeben")
root.geometry("500x400")

# Label und Eingabefelder für Benutzername, Passwort und E-Mail
label_benutzername = tk.Label(root, text="Benutzername:")
label_benutzername.pack()
entry_benutzername = tk.Entry(root)
entry_benutzername.pack()

label_passwort = tk.Label(root, text="Passwort:")
label_passwort.pack()
entry_passwort = tk.Entry(root, show="*")
entry_passwort.pack()

label_email = tk.Label(root, text="E-Mail:")
label_email.pack()
entry_email = tk.Entry(root)
entry_email.pack()

# Schaltfläche zum Einfügen der Benutzerdaten in die Datenbank
btn_insert = tk.Button(root, text="Benutzerdaten einfügen", command=insert_user)
btn_insert.pack()

# Tkinter Hauptloop starten
root.mainloop()