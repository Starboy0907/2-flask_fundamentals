from flask import Flask, redirect, request, render_template, session
app = Flask(__name__)

@app.route('/')
def checks():
    return render_template('check3.html') # Step One after file setup was to setup a route with a blank html

if __name__ == "__main__":
    app.run(debug=True)
