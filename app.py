from flask import Flask, render_template, request, redirect, send_from_directory
import requests
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'downloads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

SHEETDB_API_URL = "https://sheetdb.io/api/v1/xbi3y5ijz09uu"  # ← ONLY CHANGE THIS!

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    
    if name and email:
        try:
            data = {
                "data": [
                    {
                        "Name": name,
                        "Email": email
                    }
                ]
            }
            
            response = requests.post(SHEETDB_API_URL, json=data)
            
            if response.status_code == 201:
                return redirect('/download')
            else:
                return "Error saving your data. Please try again.", 400
                
        except Exception as e:
            return f"An error occurred: {str(e)}", 500
    
    return "Please enter both name and email.", 400

@app.route('/download')
def download():
    return send_from_directory(UPLOAD_FOLDER, 'Fat_Loss_eBook.pdf', as_attachment=True)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)