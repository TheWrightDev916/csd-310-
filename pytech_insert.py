#Anthony Wright Jr 06/20/2021 Assignment for module 5

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.rsnru.mongodb.net/pytech?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

fred = {
    "student_id": "1007",
    "first_name": "Fred",
    "last_name": "Example",
    "enrollments": [
        {
            "term": "Spring 2021",
            "gpa": "3.0",
            "start_date": "January 14, 2021",
            "end_date": "June 06, 2021",
            "courses": [
                {
                    "course_id": "NoSql3",
                    "description": "Non-Relational Databases",
                    "instructor": "Jane",
                    "grade": "B"
                },
            ]
        }
    ]

}


anthony = {
    "student_id": "1008",
    "first_name": "Anthony",
    "last_name": "Wright",
    "enrollments": [
        {
            "term": "Spring 2019",
            "gpa": "3.5",
            "start_date": "January 14, 2021",
            "end_date": "June 06, 2021",
            "courses": [
                {
                    "course_id": "Js-400",
                    "description": "Advanced Javascript",
                    "instructor": "Fishman",
                    "grade": "3.0"
                },
            ]
        }
    ]
}


nikki = {
    "student_id": "1009",
    "first_name": "Nikki",
    "last_name": "Barnes",
    "enrollments": [
        {
            "term": "Spring 2021",
            "gpa": "4.0",
            "start_date": "January 14, 2021",
            "end_date": "June 06, 2021",
            "courses": [
                {
                    "course_id": "CS-410",
                    "description": "Algorithms and Data Structures",
                    "instructor": "Chavez",
                    "grade": "4.0"
                },
            ]
        }
    ]
}
 
students = db.students

print("-- INSERT STATEMENTS --")
fred_student_id = students.insert_one(fred).inserted_id
print("Inserted student record Fred Example into the students collection with document_id" + str(fred_student_id))

anthony_student_id = students.insert_one(anthony).inserted_id
print("Inserted student record Anthony Wright into the students collection with document_id" + str(anthony_student_id))

nikki_student_id = students.insert_one(nikki).inserted_id
print("Inserted student record Nikki Barnes into the students collection with document_id" + str(nikki_student_id))

print('End of program, press any key to exit...')
