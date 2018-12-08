from flask import Flask, render_template, request, jsonify
import sqlite3
app = Flask(__name__)

#VARSHA
con = sqlite3.connect('FrostgateDetentionCenter.db')
print("Opened database successfully")

con.close()

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    result = request.form
    con = sqlite3.connect('FrostgateDetentionCenter.db', check_same_thread=False)
    crsr = con.cursor()
    query = """SELECT uname, password, OID FROM Officer"""
    crsr.execute(query)
    ans = crsr.fetchall()
    for un, pw, oid in ans:
        if un==result['username']:
            if pw==result['password']:
                return jsonify({'login': 'true', 'OID': oid})
            return jsonify({'login': 'false'})
    return jsonify({'login': 'false'})
    #return jsonify({'rows': ans})
    #if result['username']=='admin' and result['password']=='root':
    #   return jsonify({'login': 'true'})
    #return jsonify({'login': 'false'})

@app.route('/register', methods = ['POST'])
def register():
    if request.method == 'POST':
        # try:
        fname = request.form['fname']
        lname = request.form['lname']
        OID = request.form['OID']
        title = request.form['title']
        phone = request.form['phone']
        salary = request.form['salary']
        uname = request.form['uname']
        password = request.form['password']
        #VARSHA
        with sqlite3.connect("FrostgateDetentionCenter.db") as con:
            cur = con.cursor()
            #VARSHA
            cur.execute("INSERT INTO Officer VALUES (?,?,?,?,?,?,?,?)",(fname,lname,OID,title,phone,salary,uname,password))
            print(fname,lname,OID,title,phone,salary,uname,password)
            con.commit()
        # except Exception as e:
        #     print(e)
        #     con.rollback()
        # finally:
        return '200'

#VARSHAAAAA
@app.route('/add_prisoner', methods = ['POST'])
def add_prisoner():
    if request.method == 'POST':
        print(request.form)
        
        fname = request.form['fname']
        lname = request.form['lname']
        addr = request.form['addr']
        gender = request.form['gender']
        date_of_in = request.form['date_of_in']
        date_of_out = request.form['date_of_out']
        category = request.form['category']
        PID = request.form['PID']
        SID = request.form['SID']
        case_id = request.form['case_id']
        cell_id = request.form['cell_id']
        salary = request.form['salary']
        #VARSHA
        with sqlite3.connect("FrostgateDetentionCenter.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO PRISONER VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",(PID,fname,lname,addr,category,date_of_in,date_of_out,gender,salary,cell_id,SID,case_id))
            con.commit()
            print('successfully added')
        # except:
        #     con.rollback()      
        # finally:
        return '200'

@app.route('/add_warden', methods = ['POST'])
def add_warden():
    if request.method == 'POST':
        # try:
        name = request.form['name']
        WID = request.form['WID']
        OID = request.form['OID']
        salary = request.form['salary']
        #VARSHA
        with sqlite3.connect("FrostgateDetentionCenter.db") as con:
            cur = con.cursor()
            #VARSHA
            cur.execute("INSERT INTO Warden VALUES (?,?,?,?)",(name,WID,salary,OID))
            print(request.form)
            con.commit()
        # except:
        #     con.rollback()      
        # finally:
        return '200'

@app.route('/browse_officer/<oid>', methods=['GET'])
def browse_officer(oid):
    con = sqlite3.connect('FrostgateDetentionCenter.db')
    c = con.cursor()
    query = 'SELECT * FROM Warden WHERE Warden.OID='+oid
    c.execute(query)
    ans = c.fetchall()
    con.close()
    print(jsonify(ans))
    return jsonify(ans)

@app.route('/browse_warden/<wid>')
def browse_warden(wid):
    con = sqlite3.connect('FrostgateDetentionCenter.db')
    c = con.cursor()
#    query = 'SELECT * FROM Prisoner, Section WHERE Prisoner.SID=Section.SID AND WID=%s' % wid
    s = 'A_SECTION_'
    query = 'SELECT * FROM Prisoner NATURAL JOIN Section where Section.wid=%s'%wid
    #query = 'SELECT * FROM Prisoner, Section'# WHERE Prisoner.sid=Section.sid '
    c.execute(query)
    ans = c.fetchall()
    con.close()
    return jsonify(ans)

if __name__ == "__main__":
    app.run(debug=True)