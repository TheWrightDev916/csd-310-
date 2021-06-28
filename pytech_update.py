#Anthony Wright Jr 06/27/2021 Assignment for module 6.2

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.h2lbk.mongodb.net/students?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

students = db.students

docs = students.find({})
 
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in docs:
 print("Student ID: " + doc["student_id"] + "\nFirst Name: " + doc["first_name"] + "\nLast Name: " + doc["last_name"] + "\n")

result = students.update_one({"student_id": "1010"}, {"$set": {"last_name": "Jackson"}})

alex = students.find_one({"student_id": "1010"})

print("-- DISPLAYING STUDENT DOCUMENT 1010 --")

print("Student ID: " + alex["student_id"] + "\nFirst Name: " + alex["first_name"] + "\nLast Name: " + alex["last_name"] + "\n")

print("End of program, press any key to continue...")
