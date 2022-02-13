from flask import Flask
app = Flask(__name__)

@app.route('/')
def understanding():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/success')
def success():
    return "success"


if __name__ == "__main__":
    app.run(debug=True)



