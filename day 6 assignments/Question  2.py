class Student:
    def __init__(self, rollno: object, studentName: object, course: object) -> object:
        self.rollno = rollno
        self.studentName = studentName
        self.course = course
        self.marks = {}
    def __str__(self):
        return f"Roll No: {self.rollno}\nStudent Name: {self.studentName}\nCourse: {self.course}\nMarks: {self.marks}"
    def acceptStudentData(self):
        self.rollno = input("Enter Roll No: ")
        self.studentName = input("Enter Student Name: ")
        self.course = input("Enter Course: ")
        for i in range(5):
            subject = input(f"Enter Subject {i+1} Name: ")
            marks = float(input(f"Enter Marks for {subject}: "))
            self.marks[subject] = marks
    @staticmethod
    def printStudentData(studentList, rollno):
        for student in studentList:
            if student.rollno == rollno:
                print(student)
                return
        print("Student with Roll No:", rollno, "not found!")
studentList = []
for _ in range(5):
    student = Student(None, None, None)
    student.acceptStudentData()
    studentList.append(student)
rollno = input("Enter Roll No to print student data: ")
Student.printStudentData(studentList, rollno)