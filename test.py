import sqlite3
con = sqlite3.connect('FrostgateDetentionCenter.db')
c = con.cursor()
query = 'SELECT * FROM Warden WHERE Warden.OID=2222233333'
c.execute(query)
ans = c.fetchall()
con.close()
print(ans)