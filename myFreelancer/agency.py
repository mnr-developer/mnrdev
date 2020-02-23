from flask import Flask, redirect,url_for
from flask import json
from flask import render_template
from flask import request
from jinja2 import Environment, PackageLoader
from forms import ContactForm, ServiceForm
from flask_mail import Mail, Message
from portfolio import items as portfolio
from team import members as team
from error import error,error1 as error,error1
import time

env = Environment(loader=PackageLoader('agency', 'templates'))
app = Flask(__name__)
app.config.from_object('settings')
mail = Mail(app)

@app.route("/")
def index():
    return render_template("index.html",
        portfolio=portfolio,team=team
    )

# @app.route("/work")
# def work():
#     return render_template("work.html")

@app.route("/services")
def services():
    return render_template("services.html")    


# @app.route("/cases")
# def cases():
#     return render_template("blog.html") 

@app.route("/about")
def about():
    return render_template("about.html",team=team) 

# @app.route("/blog")
# def blog():
#     return render_template("blog.html")     

@app.route("/worksingle")
def worksingle():
    return render_template("worksingle.html",portfolio=portfolio)     
       

@app.route("/contact")
def contact():
    return render_template("contact.html")  

@app.route("/error")
def error():
    return render_template("error.html")   

@app.route("/success")
def success():
    return render_template("success.html")            


@app.route("/sendmsg/", methods=['GET','POST'])
def sendmsg():
    form = ContactForm(request.form)
    try:
        if form.validate():
            msg = Message(
            subject="New Subscription.",
            sender="mnrdeveloper@outlook.com",
            recipients=["mnrdeveloper@outlook.com"],
            reply_to=form.email.data,
            html=form.message.data
        )
        mail.send(msg)
        # return 'send'
        # time.sleep(1)
        #return redirect(url_for('contact'))
    # else:
    #     return json.dumps(form.errors), 400
    except:
        # return 'error'
        # time.sleep(1)
        return redirect(url_for('error'))


@app.route("/service-contact/", methods=['GET','POST'])
def service_contact():
    form = ServiceForm(request.form)
    try:
        if form.validate():
            msg = Message(
            subject="Contact form msg from "+form.email.data,
            sender="mnrdeveloper@outlook.com",
            recipients=["mnrdeveloper@outlook.com"],
            reply_to=form.email.data,
            html=form.email.data
        )
        mail.send(msg)
        return render_template('error.html',error=error)
        # return 'send'
        # time.sleep(1)
        #return redirect(url_for('contact'))
    # else:
    #     return json.dumps(form.errors), 400
    except:
        # return 'error'
        # time.sleep(1)
        return render_template('error.html',error1=error1)
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

if __name__ == "__main__":
    app.run()
