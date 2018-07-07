from flask import Flask, render_template, request, flash
from flask_mail import Mail, Message
import scrapper as sc

application = Flask(__name__)
application.secret_key = "mySecret"
application.config.from_pyfile('config.cfg')

mail = Mail(application)


@application.route('/')
def index():
    return render_template('index.html')


@application.route("/blog")
def blog():
    return render_template('blog.html')


@application.route("/connect", methods=['GET', 'POST'])
def connect():
    if request.method == 'GET':
        return render_template('connect.html')
    if request.method == "POST":
        msg = Message("Hello", [request.form['email']],
                      "Thank you for contacting, I'll try to reply as son as possible", sender='bhaskar@optimuscp.io')
        mail.send(msg)
        flash('Mail Sent!!')
        return render_template('connect.html')


@application.route("/gallery")
def gallery():
    return render_template('gallery.html', imgList=sc.imLS())


@application.route("/manage")
def manage():
    return render_template('manage.html')

@application.errorhandler(404)
def er404(e):
    return render_template('error.html', error='404')


@application.errorhandler(500)
def er500(e):
    return render_template('error.html', error='500')


if __name__ == '__main__':
    application.run()
