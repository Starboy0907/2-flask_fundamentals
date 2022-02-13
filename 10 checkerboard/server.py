from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def cb(): 
    return render_template('checkerboard.html', row=8, col=8)

@app.route('/<int:x>')
def row(x):
    return render_template('checkboard.html', row=x, col=8)

@app.route('/<int:x>/<int:y>')
def column(x,y):
    return render_template('checkerboard.html', row=x, col=y )

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def color(x,y,color1, color2):
    return render_template('checkerboard.html',x=x, y=y, color1="red", color2="black")


if __name__=="__main__":
    app.run(debug=True)