# Jr. Application Developer (STDT4) Application
**Name**: Sathvik Parasa\
**Student ID**: 922076112\
**Email**: saparasa@ucdavis.edu

---

## OA/
This folder contains the solutions to the Leetcode problems for phase 1 of the application process.

## project/
This folder contains the code to the project for phase 2 of the application process.

### project/backend
  This folder contains all the backend code for the Flask server of the project.\
- **make_csv.py**: Creates a .csv file named [persons.csv](https://github.com/sathvikparasa/JrAppDev/blob/main/project/backend/persons.csv) generating fake data (using Faker) for the backend.
- **persons.csv**: Fake data generated from make_csv.py. Data includes a unique UUIDv4, first and last names, email, and a randomly generated salary between $0 and $1,000,000.
- **requirements.txt**: File with all the required dependencies for the Flask app.py Python file.
- **app.py**: Simple Flask server that stores persons.csv in a dictionary and sends JSON data to port 8080.

**Running on your own machine.**

  Clone this repository.
  ```
  git clone https://github.com/sathvikparasa/JrAppDev.git
  cd JrAppDev/project/backend
  ```
  Make sure you set up a virtual environment.
  ```
  pip install virtualenv
  virtualenv .env
  source .env/bin/activate
  ```
  Then, install required dependencies with `pip`.
  ```
  pip install -r requirements.txt
  ```
  Then run the application.
  Method 1: python3 command
  ```
  python3 app.py
  ```
  Method 2: flask run command
  If using the command `flask run`, set the flask run port environment variable to port 8080 before the command (if you want to communicate with frontend).
  ```
  export FLASK_RUN_PORT=8080
  flask run
  ```

  On app startup, the default route will redirect you to /persons.
  Use curl or Postman to fetch request from the server, e.g. `curl http://127.0.0.1:8080/persons`
  
  **Routes:**
  - `/persons/`: Fetch data for the first 10 people in persons.csv.
  - `/persons/<user_id>/`: Fetch data for a specific UUID in persons.csv.

### project/frontend
Simple Next.js frontend styled with Tailwind. Deployed on Vercel, can be seen at [jr-app-dev.vercel.app](https://jr-app-dev.vercel.app/).

