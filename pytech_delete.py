#Anthony Wright Jr 06/27/2021 Assignment for module 6.3

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.h2lbk.mongodb.net/students?retryWrites=true&w=majority"
 
client = MongoClient(url)

db = client.pytech

students = db.students
 
studentDocs = students.find({})
 
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY--")

for doc in studentDocs:
    print("Student ID: " + doc["student_id"] + "\nFirst Name: " + doc["first_name"] + "\nLast Name: " + doc["last_name"] + "\n")

appDoc = {
    "student_id": "1010",
    "first_name": "Alex",
    "last_name": "Horne"
}
 
insertDoc = students.insert_one(appDoc).inserted_id
 
print("-- INSERT STATEMENTS --")
print("Inserted student record into the students collection with document_id " + str(insertDoc))

student_appDoc = students.find_one({"student_id": "1010"})
 
print("-- DISPLAYING STUDENT TEST DOC -- ")
print("Student ID: " + student_appDoc["student_id"] + "First Name: " + student_appDoc["first_name"] + "Last Name: " + student_appDoc["last_name"] + "\n")

deleted_student_appDoc = students.delete_one({"student_id": "1010"})
 
studentDocs2 = students.find({})

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY--")

for doc in studentDocs2:
 print("Student ID: " + doc["student_id"] + "\nFirst Name: " + doc["first_name"] + "\nLast Name: " + doc["last_name"] + "\n")

print("End of program, press any key to continue...")
