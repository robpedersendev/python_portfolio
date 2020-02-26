from flask import Flask, redirect, render_template, request  # send_from_directory

import csv

# import os


app = Flask(__name__)


# print(__name__)

@app.route('/')  # This is a python decorator
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')  # This is a python decorator
def dynamic_routing(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a')as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n {email} - {subject}: {message}')


def write_to_csv(data):
    with open('database.csv', mode='a+', newline="")as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thanks.html')
        except:
            return 'An error occurred and this was not saved to the database'
    else:
        return 'Something went wrong'
