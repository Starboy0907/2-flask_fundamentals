from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo'

@app.route('/say/<string:name>')
def say(name):
    print(name)
    return 'Hi, ' + name

@app.route('/<string:name>/<int:num>')
def repeat(name, num):
    output = ''
    for i in range(0,num):
        output += f"<p>{name}</p>"
    return output


if __name__=="__main__":
    app.run(debug=True)
    
