from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

@app.route('/') # this is a reroute function for whrn the index page is not the base url
def new_route():
    return redirect('/play')

@app.route('/play') #this is the actual index page 
def level_one(): # we are just rendering template and not passing in any arguments at this juncture
    return render_template('colored_boxes.html', num=3, color="blue") # the 

@app.route('/play/<int:num>')
def level_two(num):
    return render_template('colored_boxes.html',num=num, color="blue" )

if __name__ == "__main__":
    app.run(debug=True)  