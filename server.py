from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name) 

def write_to_file(data):
    with open('database.txt', 'a') as database:
        name = data['name']
        message = data['message']
        email = data['email']
        file = database.write(f'\n{name},{email},{message}')

def write_to_csv(data):
    with open('database.csv', 'a',newline='') as database2:
        name = data['name']
        message = data['message']
        email = data['email']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'something went wrong. Try again'