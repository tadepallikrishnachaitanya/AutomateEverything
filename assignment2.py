class Student:
    def __init__(self, rollno, name, subject, totalmarks):
        self.rollno=rollno
        self.name=name
        self.subject=subject
        self.totalmarks=totalmarks
        #print(rollno, name, subject, totalmarks)

    def displayData(self):
        print(f"The rollno, name, subject and totalmarks of the student are: {self.rollno}, {self.name}, {self.subject} and {self.totalmarks}")

    # display the object into human readable string we use __str__
    def __str__(self):
        return f"{self.rollno}, {self.name}, {self.subject}, {self.totalmarks}"

student=Student("234", "Krishna", "Science", 75)
print(student)
#student.displayData()
