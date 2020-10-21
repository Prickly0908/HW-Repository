import json

class Person:
    def __init__(self, name, email, phone, address):
        self.first_name = name['first']
        self.last_name = name['last']
        self.email = email
        self.phone = phone
        self.address = address

    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)

    def __repr__(self):
        return f'<{ self.first_name, self.last_name}>'

students_list = []
with open('students.json', 'r') as json_file:
    student_data = json.loads(json_file.read())
    for u in student_data['persons']['students']:
        students_list.append(Person(**u))

teacher_list=[]
with open('students.json','r') as json_file:
    teacher_data = json.loads(json_file.read())
    for u in teacher_data['persons']['teacher']:
        teacher_list.append(Person(**u))

print(f'Student:{students_list}')

print(f'Tutor:{teacher_list}')


