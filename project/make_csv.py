import faker
import random
import uuid
import csv

fake = faker.Faker()

headers = ["Id, First_Name, Last_Name, Email, Salary"]

with open('data.csv', 'w', newline='') as file:
    writer  = csv.writer(file)
    writer.writerow(headers)

    for i in range(100):
        uid = str(uuid.uuid4())
        name = fake.name().split()
        
        first = name[0]
        last = name[1]

        email = first[0].lower() + last.lower() + '@gmail.com'
        salary = round(random.uniform(0, 1000000), 2)

        row = [uid, first, last, email, salary]
        writer.writerow(row)
