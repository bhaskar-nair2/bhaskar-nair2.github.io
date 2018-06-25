from flask import Flask, render_template, request, flash
from flask_mail import Mail,Message
import scrapper as sc


app = Flask(__name__)
app.secret_key="mySecret"

app.config['MAIL_SERVER'] = 'smtp.zoho.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config.from_pyfile('config.cfg')

mail=Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route("/connect",methods=['GET','POST'])
def connect():
    if request.method=='GET':
        return render_template('connect.html')
    if request.method=="POST":
        msg=Message("Hello",[request.form['email']],"Thank you for contacting, I'll try to reply as son as possible",sender='bhaskar@optimuscp.io')
        mail.send(msg)
        flash('Mail Sent!!')
        return render_template('connect.html')

@app.route("/gallery")
def gallery():
    return render_template('gallery.html',imgList=sc.imLS())

@app.errorhandler(404)
def er404(e):
    return render_template('error.html',error = '404')

@app.errorhandler(500)
def er500(e):
    return render_template('error.html',error = '500')

if __name__ == '__main__':
    app.run(debug=True)
