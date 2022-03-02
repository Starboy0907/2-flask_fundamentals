from flask import Flask, render_template, request, redirect, session
from datetime import datetime
app = Flask(__name__)
app.secret_key = "super secret pizza"

language_dict= {
    'python': 'Python',
    'c_sharp': 'C#',
    'rust': 'Rust',
    'ruby': 'Ruby'
}

language_list = ['Python', 'C#']

@app.route('/')
def indexing():
    return "Hello Babe!"

# @app.route('/')
# def index():
#     render_template('index.html')

@app.route('/process', methods = ["POST"])
def process():
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['pet_name'] = request.form['pet_name']
    return redirect('results.html')

@app.route('/order')
def post_to_render():
    order_total = int(request.form['quantity'])* int(request.form['price'])
    print(f"Charged credit card: ${order_total} at {datatime.now()}")
    return render_template("/order_receipt.html", quantity= request.form['quantity'], order_total = order_total)

@app.route("/purchase/redirect", methods = ['POST'])
def post_to_redirect():
    session['order_total']= int(request.form['quantity'])* int[request.form['price']]
    (request.form['price'])
    session['quantity'] = request.form['quantity']

    print(f"Charged credit card: ${session['order_total']}{datetime.now()}")

@app.route('/order/results')
def order_results():
    return render_template('order_receipt,html')

if __name__ == "__main__":
    app.run(debug=True)

