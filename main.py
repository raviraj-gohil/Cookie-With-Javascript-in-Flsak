from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home.html')

@app.route("/profie", methods = ['POST','GET'])
def success():
    return "login success"


if __name__ == '__main__':
    app.run(debug=True)




