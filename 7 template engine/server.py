from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", phrase="hello", times=5) #notice the two named arguments!

if __name__=="__main__":
    app.run(debug=True)
