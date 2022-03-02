from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
#localhost: 5000
def hello_worlds():
    return render_template('layout.html', user=guest)

@app.route('/child')
def child():
    return render_template('child.html')



#localhost:5000/greeting
@app.route("/greeting")
def greetings():
    return "this is a generic greeting"

@app.route("/greeting/<guest>") #parameter 
def guest(guest): #argument
    print(guest)  #argument
    return render_template('layout.html', user=guest)

@app.route('/greeting/<guest>/<best>')
def best(guest, best):
    example_db_data = [
        {"id": 1, "first_name": "Marge", "last_name": "Simpson"},
        {"id": 2, "first_name": "Homer", "last_name": "Simpson"},
        {"id": 3, "first_name": "Lisa", "last_name": "Simpson"},
        {"id": 4, "first_name": "Bart", "last_name": "Simpson"},
        {"id": 5, "first_name": "Hana", "last_name": "Simpson"},
    ]
    print(guest, best)
    return render_template('child.html', user=guest, loser=best, users = example_db_data)


if __name__ == "__main__":
    app.run(debug=True)








