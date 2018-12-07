import sqlite3
with sqlite3.connect("FrostgateDetentionCenter.db") as con:
     cur = con.cursor()
     cur.execute("INSERT INTO Warden VALUES (?,?,?,?)",('Manuzo', '1122334456', 100, '1111111111'))
     con.commit()
