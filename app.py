
from flask import Flask, render_template, request, redirect, send_from_directory
import csv
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'downloads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    if name and email:
        with open('submissions.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([name, email])
        return redirect('/download')
    return "Please enter both name and email.", 400

@app.route('/download')
def download():
    return send_from_directory(UPLOAD_FOLDER, 'Fat_Loss_eBook.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
