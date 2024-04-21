class Course:
    def __init__(self, name, fees):
        self.name = name
        self.fees = fees

    def accept_data(self):
        self.name = input("Enter the name of the course: ")
        self.fees = input("Enter the fees for the course: ")

    def print_data(self):
        print(f"Course Name: {self.name}")
        print(f"Fees: {self.fees}")


class Computer(Course):
    def __init__(self, name, fees, subjectList):
        super().__init__(name, fees)
        self.subjectList = subjectList

    def accept_data(self):
        super().accept_data()
        self.subjectList = input("Enter the subjects for the computer course (comma-separated): ").split(",")

    def print_data(self):
        super().print_data()
        print(f"Subjects: {', '.join(self.subjectList)}")


class Electronics(Course):
    def __init__(self, name, fees, subjectList):
        super().__init__(name, fees)
        self.subjectList = subjectList

    def accept_data(self):
        super().accept_data()
        self.subjectList = input("Enter the subjects for the electronics course (comma-separated): ").split(",")

    def print_data(self):
        super().print_data()
        print(f"Subjects: {', '.join(self.subjectList)}")


while True:
    print("1. Create a Course")
    print("2. Create a Computer Course")
    print("3. Create an Electronics Course")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        course = Course("", "")
        course.accept_data()
        course.print_data()
    elif choice == "2":
        computer = Computer("", "", [])
        computer.accept_data()
        computer.print_data()
    elif choice == "3":
        electronics = Electronics("", "", [])
        electronics.accept_data()
        electronics.print_data()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
