import faker
import random
import uuid
import csv

# Use Faker to create fake data for names
fake = faker.Faker()

# Headers for csv file
headers = ["Id, First_Name, Last_Name, Email, Salary"]

# Create data.csv file and write to it
with open('persons.csv', 'w', newline='') as file:
    writer  = csv.writer(file)
    writer.writerow(headers)

    for i in range(100):
        # Get unique uid with uuid library
        uid = str(uuid.uuid4())

        # Get name from fake.name() and split to first and last
        name = fake.name().split()
        first = name[0]
        last = name[1]

        # Make sure no suffixes are the first name
        if first in ["Mrs.", "Dr.", "Mr.", "Ms.", "Lt.", "Sir"]:
            first = name[1]
            last = name[2]

        # Email is the first letter of first name + last name + @gmail.com
        email = first[0].lower() + last.lower() + '@gmail.com'
        
        # Salary is random float from $0 to $1,000,000
        salary = f"{round(random.uniform(0, 1000000), 2):.2f}"
        # I had to change salary itself to a string for 2 decimal rounding 
        #   but it doesn't matter in a csv file

        # Write row of data to csv file
        row = [uid, first, last, email, salary]
        writer.writerow(row)
