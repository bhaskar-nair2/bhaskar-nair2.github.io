from flask import Flask, render_template, request, flash
from saveMail import Mailer
import scrapper as sc

## EB Container: flask-env

application = Flask(__name__)
application.secret_key = "mySecret"
application.config['MAIL_SERVER'] = 'smtp.zoho.com'
application.config['MAIL_PORT'] = 465
application.config['MAIL_USE_SSL'] = True
application.config.from_pyfile('config.cfg')

mail = Mailer(application)


@application.route('/')
def index():
    return render_template('index.html')


@application.route("/blog")
def blog():
    return render_template('blog.html')


@application.route("/connect", methods=['GET', 'POST'])
def connect():
    if request.method == "POST":
        if not (request.form['email'] is None and request.form['subject'] is None and request.form['content'] is None):

            # msgme = Message(subject=request.form['email'], recipients='bhaskar@optimuscp.io',body=request.form['content'], html=request.form['subject'], sender='noreply@bhaskarnair.me')

            mail.sendThanks(request.form)
            mail.sendMe(request.form)
            flash('Mail Sent!!')
        else:
            flash('Fields Empty')
    return render_template('connect.html')


@application.route("/gallery")
def gallery():
    return render_template('gallery.html', imgList=sc.imLS())


@application.route("/manage", methods=["Get", "POST"])
def manage():
    if request.method == 'GET':
        return render_template('manage.html', val=False)
    if request.method == 'POST':
        return "Inside Panel"


@application.errorhandler(404)
def er404(e):
    return render_template('error.html', error='404')


@application.errorhandler(500)
def er500(e):
    return render_template('error.html', error='500')


if __name__ == '__main__':
    application.run(host='0.0.0.0')
