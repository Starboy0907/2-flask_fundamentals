from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    order_info = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'student_id': request.form['student_id'],
        'apple': request.form['apple'],
        'raspberry': request.form['raspberry'],
        'strawberry': request.form['strawberry']

    }
    
    count = int(order_info['apple'])+int(order_info['raspberry'])+int(order_info['strawberry'])

    print(count)
    
    print(request.form)
    print(request.form['first_name'])
    return render_template("checkout.html", orders = order_info, count = count)


@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    