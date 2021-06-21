Anthony Wright Jr 06/20/2021 Assignment for module 5

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.rsnru.mongodb.net/pytech?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

students = db.students

docs = students.find({})

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")


for doc in docs:
    print(doc)


fred = students.find_one({"student_id": "1007"})
 
print("-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print(doc["student_id"])


print("End of program, press any key to continue...")
