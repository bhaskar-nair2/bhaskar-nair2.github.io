from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route("/connect")
def connect():
    return render_template('contact.html')

@app.route("/gallery")
def gallery():
    return render_template('gallery.html')

@app.errorhandler(404)
def er404(e):
    return render_template('error.html',error = '404')

if __name__ == '__main__':
    app.run(debug = True)
