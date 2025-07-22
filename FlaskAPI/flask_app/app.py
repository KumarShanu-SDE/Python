from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

from pymongo import MongoClient
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MongoDB Connection
client = MongoClient('mongodb+srv://kumarsha:<password>@cluster0.xaa2qev.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

db = client.get_database('my_database')
users_collection = db.users

@app.route('/api', methods=['GET'])
def get_data():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/submit', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        try:
            # Get data from the form
            name = request.form['name']
            email = request.form['email']
            
            # Insert data into MongoDB
            user_data = {'name': name, 'email': email}
            users_collection.insert_one(user_data)
            
            # Redirect to success page
            return redirect(url_for('success'))
        except Exception as e:
            flash(f"Error: {str(e)}")
            return render_template('submit_form.html')
    
    return render_template('submit_form.html')

@app.route('/success')
def success():
    return "Data submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
