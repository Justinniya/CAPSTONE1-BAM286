from flask import Flask, render_template, url_for, redirect, request,session
from flask_mysqldb import MySQL 
import os
#need download sang flask_mysqldb (DONE)

app = Flask(__name__)
mysql = MySQL(app)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "mitscoop"
app.secret_key = "mitscoop"
UPLOAD_FOLDER = 'static/uploads'
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER,exist_ok=True)

@app.route('/')
def landingpage():
    return render_template("login.html")

#iya namn ni sang userame kag password para sa ma log-in 
@app.route('/index',methods = ["GET","POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        pwd = request.form["password"]
        cursor = mysql.connection.cursor()
        cursor.execute(f"INSERT INTO users(name,password)VALUES(%s, %s)",(name, pwd))
        cursor.connection.commit()
        return redirect(url_for("login"))
    return render_template("login.html")

#iya ni sang registration nga connection, landing page to sql using flask !! 
@app.route('/register',methods = ["GET","POST"])
def registration():
   if request.method == "POST":
       nm = request.form["nm"]
       age = request.form["age"]
       gen = request.form["gen"]
       add = request.form["add"]
       stat = request.form["stat"]
       cn = request.form["cn"]
       wk = request.form["wk"]
       uname = request.form["Username"]
       password = request.form["Password"]
       confirm_password = request.form['con_password']
       cursor = mysql.connection.cursor()
       cursor.execute(f"SELECT * FROM users WHERE username = %s",(uname,))
       user = cursor.fetchone()
       if user:
           return redirect('/register')
       else:
           if password == confirm_password:
               cursor = mysql.connection.cursor()
               cursor.execute(f"INSERT INTO users VALUES(0,%s, %s,%s, %s,%s, %s,%s,%s,%s)",(nm, age,gen,add,stat,cn,wk,uname,password))
               cursor.connection.commit()
               return redirect("/login")
           else:
               return redirect('/register')
                
   else:
       return render_template("registration.html")

#iya namn ni sang admin nga registration pra nd mag sala ang mag register like employee kg admin
@app.route('/ad_register',methods = ["GET","POST"])
def ad_register():
   if request.method == "POST":
       nm = request.form["nm"]
       age = request.form["age"]
       gen = request.form["gen"]
       add = request.form["add"]
       stat = request.form["stat"]
       cn = request.form["cn"]
       username = request.form["Username"]
       password = request.form["Password"]
       cursor = mysql.connection.cursor()
       cursor.execute(f"INSERT INTO admin_users VALUES(0,%s, %s,%s, %s,%s, %s,%s,%s)",(nm, age,gen,add,stat,cn,username,password))
       cursor.connection.commit()
       return redirect(url_for("login"))
   return render_template("admin_reg.html")  

# log in tapos pwede ka select if admin or employee
@app.route('/login',methods = ["GET","POST"])
def login():
    if request.method == "POST":
        name = request.form["username"]
        pwd = request.form["password"]
        work_post = request.form["work_position"]
        cursor = mysql.connection.cursor()
        print(name,pwd)
        if work_post == "Admin": # diri gina check if admin sys or hnd
            cursor.execute(f"SELECT * FROM admin_users WHERE username = %s AND password = %s ",(name,pwd))
            user = cursor.fetchone()
            if user:
                session['admin_id'] = user[0] #session para sa admin
                return redirect("/emp_as_admin")
            else:
                print("error")
                return redirect(url_for("login"))
        else:
            cursor.execute(f"SELECT * FROM users WHERE username = %s AND password = %s ",(name,pwd))
            user = cursor.fetchone()
            if user:
                session['user_id'] = user[0] #session para sa users
                return redirect("/emp_dashboard")
            else:
                print("error")
                return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/emp_dashboard")
def employee_dashboard():
    user_id = session.get("user_id")
    return render_template("employee_dashboard.html",user_id=user_id)

@app.route('/emp_profile')
def emp_acc():
    cursor = mysql.connection.cursor()
    user_id = session.get("user_id")
    cursor.execute(f"SELECT * FROM users Where user_id = {user_id}")
    ad_user = [cursor.fetchone()]
    
    return render_template("employee_profile.html",ad_user=ad_user)

@app.route('/view_performance')
def performance():
    return render_template('emp_view_performance.html')

@app.route("/message_report",methods=["GET","POST"])
def message_report():
    id = session.get("user_id")
    cursor = mysql.connection.cursor()
    cursor.execute(f"SELECT name FROM users WHERE user_id = {id}")
    result = cursor.fetchone()
    if request.method == "POST":
        message = request.form["message"]
        image = request.files["image"]
        image_path = None
        if image and image.filename:
            image_path = app.config['UPLOAD_FOLDER']+'/'+image.filename
            image.save(image_path)
        cursor = mysql.connection.cursor()
        cursor.execute(f"INSERT INTO message_report VALUES(0,%s,%s,%s,%s)",(id,message,result,image_path))
        cursor.connection.commit()
        return redirect('/message_report')
    else:
        return render_template("employee_send_report.html")
    
@app.route('/check_report')
def check_report():
    return render_template('employee_view_perf.html')

@app.route("/message_report/delete/<string:id>")
def message_report_delete(id):
    cursor = mysql.connection.cursor()
    cursor.execute(f"DELETE FROM message_report WHERE id = {id}")
    cursor.connection.commit()
    return redirect('/admin/message_report')

@app.route('/emp_db')
def emp_db():
    return render_template("emp_db.html")

@app.route('/emp_as_admin')
def emp_as_admin():
    admin_id = session.get("admin_id") # session sang naka log in nga admin

    if admin_id:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE work_post = 'Admin'")
        admins = cursor.fetchall()
        return render_template("admin_dashboard.html",admins=admins,admin_id=admin_id)
    else:
        return redirect('/')

@app.route('/confirm/<string:id>')
def confirm_user(id):
    cursor = mysql.connection.cursor()
    cursor.execute(f"SELECT * FROM users WHERE user_id = {id}") #eh check sang system ang account sang admin nga nag register sa users table
    result = cursor.fetchone()
    cursor.execute(f"INSERT INTO admin_users VALUES(0,%s, %s,%s, %s,%s, %s,%s,%s)",(result[1],result[2],result[3],result[4],result[5],result[6],result[8],result[9])) # tapos isaylo naton and data halin sa user pa kagto sa may admin_user
    cursor.connection.commit()
    cursor.execute(f"DELETE FROM users WHERE user_id = {id}") # after sina dulaon na naton ang data nga ara sa users kay na pasa na ang data sa admin user
    cursor.connection.commit()
    return redirect('/emp_as_admin')
    

@app.route('/delete/<string:id>')
def delete_user(id):
    cursor = mysql.connection.cursor()
    cursor.execute(f"DELETE FROM users WHERE user_id = {id}") # decline ni sya if nag pinagusto sa register as admin
    cursor.connection.commit()
    return redirect('/emp_as_admin')

@app.route('/admin_profile/<string:id>')
def admin_acc(id):
    cursor = mysql.connection.cursor()
    cursor.execute(f"SELECT * FROM admin_users Where admin_id = {id}")
    ad_user = [cursor.fetchone()]
    return render_template("admin_profile.html",ad_user=ad_user)



@app.route('/admin/message_report')
def ad_message_report():
    admin_id = session.get("admin_id")
    if admin_id:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM message_report")
        messages = cursor.fetchall()
        return render_template("admin_message_report.html",messages=messages,admin_id=admin_id)
    else:
        return redirect('/')
@app.route('/admin/ad_monitor_performance')
def admin_monitor_performance():
    return render_template('admin_monitor_perf.html')

@app.route('/admin/ad_user')
def admin_user():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM admin_users")
    ad_user = cursor.fetchall()
    return render_template("profile.html",ad_user=ad_user)

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')



if __name__ == "__main__":
    app.debug=True 
    app.run()