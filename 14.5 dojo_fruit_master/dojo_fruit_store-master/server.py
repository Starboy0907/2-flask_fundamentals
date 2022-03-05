from flask import Flask, render_template, request, redirect
from datetime import datetime
date = datetime.now()
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    a = request.form['strawberry']
    print(a)
    b = request.form['raspberry']
    c = request.form['apple']
    x = request.form['first_name']
    y=  request.form['last_name']
    z=  request.form['student_id']    
    return render_template("checkout.html",a=a,b=b,c=c,x=x,y=y,z=z, quantity=int(float(a))+ int(float(b))+ int(float(c)), charge_time=date.strftime("%c") )

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    