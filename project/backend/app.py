import os
from flask import Flask, jsonify, redirect
from flask_cors import CORS
import csv

app = Flask(__name__)
# Add cross origin resource sharing for Nextjs frontend
CORS(app)

# List of already seen UUIDs
seen_ids = []

# Store json data in this list
persons_list = []

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
            # If row is not valid, skip it
            if(validate_row(row)):
                row["Salary"] = float(row["Salary"])
                persons_list.append(row)

@app.route("/", methods=["GET"])
def index():
    return redirect("/persons")

@app.route("/persons", methods=["GET"])
def persons():
    # Load data and hold it in json format / list of dictionaries
    csv_json()
    # Return first 10 people
    return jsonify(persons_list[:10])

@app.route("/persons/<user_id>", methods=["GET"])
def find_person(user_id):
    if not persons_list:
        # If user has not gone to /persons before this route,
        # Load the data
        csv_json()
    
    # Iterate over all the persons to find the matching [id]
    # Only 100 values so O(n) isn't too big a concern
    for person in persons_list:
        if person["Id"] == user_id:
            return jsonify(person)

    # Error handling    
    return jsonify(404, "Person not found")

if __name__ == '__main__':
    # Listening on port 8080
    app.run(debug=True, port=8080)