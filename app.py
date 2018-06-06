from flask import Flask, render_template
import scrapper as sc

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route("/connect")
def connect():
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
    app.run(debug = True,host='18.218.187.182',port=5000)
