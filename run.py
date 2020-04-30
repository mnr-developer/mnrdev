from flask import Flask, redirect,url_for , session, flash, url_for
from flask import json
from flask import render_template
from flask import request
from jinja2 import Environment, PackageLoader
from forms import ContactForm, ServiceForm
from flask_mail import Mail, Message
from portfolio import items as portfolio
from team import members as team
from error import error,error1 as error,error1
import os
import datetime
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename


env = Environment(loader=PackageLoader('run', 'templates'))
app = Flask(__name__)
app.config.from_object('settings')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'phpmyadmin'
app.config['MYSQL_PASSWORD'] = 'Mnr@mab1'
app.config['MYSQL_DB'] = 'mnrdev'
app.secret_key = 'thisismysecretkettemporary'

UPLOAD_FOLDER = 'static/images'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

mail = Mail(app)
mysql = MySQL(app)


# @app.route("/dbcheck")
# def dbcheck():
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM tbl_users")
#     result = cur.fetchall()
#     return str(result)
# if request.method == "POST":
#         details = request.form
#         firstName = details['fname']
#         lastName = details['lname']
#         cur = mysql.connection.cursor()
#         cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
#         mysql.connection.commit()
#         cur.close()
#         return 'success'
#     return render_template('index.html')

#something = cur.fetchone()

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == "POST":
        details = request.form
        email = details['email']
        dated = datetime.datetime.now()
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tbl_subscribers(email,dated) VALUES ('%s','%s')" % (email,dated) )
        mysql.connection.commit()
        cur.close()
    return render_template("index.html",portfolio=portfolio,team=team)

# @app.route("/work")
# def work():
#     return render_template("work.html")

@app.route("/services")
def services():
    return render_template("services.html")    

@app.route("/loggedin", methods=['GET','POST'])
def loggedin():
 # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST':
        # Create variables for easy access
        email = request.form['email']
        password = request.form['password']
        # Check if account exists using MySQL
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM tbl_user WHERE email = '%s' AND pswd = '%s'" % (email, password))
        # Fetch one record and return result
        account = cur.fetchone()
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account[0]
            session['email'] = account[1]
            # Redirect to home page
            msg =  'Logged in successfully!'
            return render_template('profile.html')
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('login.html', msg=msg)   

@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('admin'))


@app.route("/login")
def cases():
    return render_template("login.html") 

# @app.route("/dashboard")
# def dashboard():
#     return render_template("dashboard.html")     

@app.route("/about", methods=['GET','POST'])
def about():
    return render_template("about.html",team=team) 

@app.route("/blog")
def blog():
    return render_template("blog.html")     

@app.route("/worksingle")
def worksingle():
    return render_template("worksingle.html",portfolio=portfolio)     
       

@app.route("/contact", methods=['GET','POST'])
def contact():
    if request.method == "POST":
        details = request.form
        name = details['name']
        email = details['email']
        phone = details['phone']
        message = details['message']
        dated = datetime.datetime.now()
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tbl_contact(name,email,phone,message,dated) VALUES ('%s','%s','%s','%s','%s')" % (name,email,phone,message,dated) )
        mysql.connection.commit()
        cur.close()
    return render_template("contact.html")  

# @app.route("/error")
# def error():
#     return render_template("error.html")   

# @app.route("/success")
# def success():
#     return render_template("success.html")            


# @app.route("/sendmsg/", methods=['GET','POST'])
# def sendmsg():
#     form = ContactForm(request.form)
#     try:
#         if form.validate():
#             msg = Message(
#             subject="New Subscription.",
#             sender="mnrdev@outlook.com",
#             recipients=["mnrdev@outlook.com"],
#             reply_to=form.email.data,
#             html=form.message.data
#         )
#         mail.send(msg)
#         # return 'send'
#         # time.sleep(1)
#         #return redirect(url_for('contact'))
#     # else:
#     #     return json.dumps(form.errors), 400
#     except:
#         # return 'error'
#         # time.sleep(1)
#         return redirect(url_for('error'))


# @app.route("/service-contact/", methods=['GET','POST'])
# def service_contact():
#     form = ServiceForm(request.form)
#     try:
#         if form.validate():
#             msg = Message(
#             subject="Contact form msg from "+form.email.data,
#             sender="mnrdeveloper@outlook.com",
#             recipients=["mnrdeveloper@outlook.com"],
#             reply_to=form.email.data,
#             html=form.email.data
#         )
#         mail.send(msg)
#         return render_template('error.html',error=error)
#         # return 'send'
#         # time.sleep(1)
#         #return redirect(url_for('contact'))
#     # else:
#     #     return json.dumps(form.errors), 400
#     except:
#         # return 'error'
#         # time.sleep(1)
#         return render_template('error.html',error1=error1)
# def filter_by(service_name):
#     return lambda x: service_name in x.get("service").lower()

# android_portfolio = filter(filter_by("android"), portfolio)
# ios_portfolio = filter(filter_by("ios"), portfolio)
# web_portfolio = filter(filter_by("web"), portfolio)

# @app.route("/android-services/", methods=['GET'])
# def android():
#     return render_template("work-single.html", portfolios=android_portfolio, service_name="android")

# @app.route("/ios-services/", methods=['GET'])
# def ios():
#     return render_template("ios.html", portfolios=ios_portfolio, service_name="ios")

# @app.route("/web-development-services/", methods=['GET'])
# def web():
#     return render_template("web.html", portfolios=web_portfolio, service_name="web")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']
#         # if user does not select file, browser also
#         # submit an empty part without filename
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


@app.route("/profile", methods=['GET','POST'])
def profile():
    if request.method == "POST":
        details = request.form
        email = details['email']
        username = details['username']
        password = details['pswd']
        confirm = details['cpswd']
        #dated = datetime.datetime.now()
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM tbl_user")
        mysql.connection.commit()
        cur.close() 
        if username :
            cur = mysql.connection.cursor()
            cur.execute("UPDATE tbl_user SET username='%s'"%(username))
            mysql.connection.commit()
            cur.close() 
            flash("All Details Updated Successfully")
        elif email:
            cur = mysql.connection.cursor()
            cur.execute("UPDATE tbl_user SET email='%s'"%(email) )
            mysql.connection.commit()
            cur.close() 
            flash("All Details Updated Successfully")
        elif email & username:
            cur = mysql.connection.cursor()
            cur.execute("UPDATE tbl_user SET username='%s', email='%s'"%(username,email))
            mysql.connection.commit()
            cur.close() 
            flash("All Details Updated Successfully")
        elif email & username & password :
            if password == confirm:
                cur = mysql.connection.cursor()
                cur.execute("UPDATE tbl_user SET username='%s', pswd='%s', email='%s'" %(username,password,email) )
                mysql.connection.commit()
                cur.close() 
                flash("All Details Updated Successfully")
            else:
                flash("Password Does not match")
        elif password & confirm:
            if password == confirm:
                cur = mysql.connection.cursor()
                cur.execute("UPDATE tbl_user SET pswd='password'" )
                mysql.connection.commit()
                cur.close() 
                flash("All Details Updated Successfully")
            else:
                flash("Password Does not match")   
        else:
            flash("Please Check the Form Carefully")             
    return render_template("profile.html")

@app.route("/aboutDash", methods=['GET','POST'])
def aboutDash():
    if request.method == "POST":
        details = request.form
        site_title = details['site_title']
        description = details['desc']
        address = details['address']
        contact = details['contact']
        aboutme1 = details['about_1']
        aboutme2 = details['about_2']
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM tbl_user")
        mysql.connection.commit()
        cur.close() 
        #check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        dated = datetime.datetime.now()
        cur = mysql.connection.cursor()
        cur.execute("UPDATE tbl_user SET site_title = '%s', description='%s', address='%s', photo='%s', about_1 = '%s', about_2='%s', contact_no = '%s', updated_date='%s'" %(site_title,description,address,filename,aboutme1,aboutme2,contact,dated))
        mysql.connection.commit()
        cur.close()
    return render_template("addAbout.html")

@app.route("/blogDash", methods=['GET','POST'])
def blogDash():
    if request.method == "POST":
        details = request.form
        title = details['title']
        link = details['link']
        description = details['description']
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM tbl_user")
        mysql.connection.commit()
        cur.close() 
        #check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        dated = datetime.datetime.now()
        cur = mysql.connection.cursor()
        cur.execute("UPDATE tbl_caseStudy SET photo = '%s', title='%s', description='%s', link='%s', date = '%s'" %(filename,title,description,link,dated))
        mysql.connection.commit()
        cur.close()
    return render_template("addBlog.html")

@app.route("/work", methods=['GET','POST'])
def work():
    if request.method == "POST":
        details = request.form
        site_name = details['site_name']
        site_link = details['site_link']
        description = details['site_description']
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM tbl_user")
        mysql.connection.commit()
        cur.close() 
        #check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        dated = datetime.datetime.now()
        cur = mysql.connection.cursor()
        cur.execute("UPDATE tbl_myWork SET photo = '%s', site_name='%s', site_description='%s', link='%s', dated = '%s'" %(filename,site_name,description,site_link,dated))
        mysql.connection.commit()
        cur.close()
    return render_template("addWork.html")       

@app.route("/comment", methods=['GET','POST'])
def comment():
    # if request.method == "POST":
    #     details = request.form
    #     email = details['email']
    #     dated = datetime.datetime.now()
    #     cur = mysql.connection.cursor()
    #     cur.execute("INSERT INTO tbl_subscribers(email,dated) VALUES ('%s','%s')" % (email,dated) )
    #     mysql.connection.commit()
    #     cur.close()
    return render_template("comments.html")   


if __name__ == "__main__":
    app.run(debug=True ,port= 12345)
