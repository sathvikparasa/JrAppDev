import os
from flask import Flask, jsonify
from flask_cors import CORS
import csv

app = Flask(__name__)
CORS(app)

# List of already seen UUIDs
seen_ids = []
data = []

def validate_row(row):
    # Validate non-empty unique UUID v4
    if (row['Id'] in seen_ids) or (not row['Id']):
        return False
    # Add to list of seen ids
    seen_ids.append(row["Id"])

    # Validate first name, last name, and email
    if not row["First_Name"] or not row["Last_Name"] or not row["Email"]:
        return False

    # Properly formatted Salary to be converted back to float from string
    try:
        float(row['Salary'])
    except ValueError:
        return False

    return True

def csv_json():
    with open('persons.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if(validate_row(row)):
                row["Salary"] = float(row["Salary"])
                data.append(row)
            else:
                data.append("ERROR APPENDING ROW. INVALID FIELD.")

@app.route("/persons", methods=["GET"])
def persons():
    csv_json()
    return jsonify(data[:10])

@app.route("/persons/<user_id>", methods=["GET"])
def find_person(user_id):
    if not data:
        csv_json()
    
    for person in data:
        if person["Id"] == user_id:
            return jsonify(person)
        
    return jsonify(f"Person with UUID {user_id} not found.")

if __name__ == '__main__':
    app.run(debug=True, port=8080)