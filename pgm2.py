class Student:
    def __init__(self, student_id, name, department, year):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.year = year

    def display(self):
        print("\nStudent Details")
        print("----------------")
        print(f"ID        : {self.student_id}")
        print(f"Name      : {self.name}")
        print(f"Department: {self.department}")
        print(f"Year      : {self.year}")


class StudentRegistrationSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        try:
            student_id = int(input("Enter Student ID: "))
            name = input("Enter Student Name: ")
            department = input("Enter Department: ")
            year = int(input("Enter Year (1-4): "))

            student = Student(student_id, name, department, year)
            self.students.append(student)
            print("\nStudent registered successfully!")

        except ValueError:
            print("\nInvalid input. Please enter correct details.")

    def view_students(self):
        if not self.students:
            print("\nNo students registered yet.")
        else:
            for student in self.students:
                student.display()

    def search_student(self):
        search_id = int(input("Enter Student ID to search: "))
        for student in self.students:
            if student.student_id == search_id:
                student.display()
                return
        print("\nStudent not found.")

    def delete_student(self):
        delete_id = int(input("Enter Student ID to delete: "))
        for student in self.students:
            if student.student_id == delete_id:
                self.students.remove(student)
                print("\nStudent deleted successfully.")
                return
        print("\nStudent not found.")

    def menu(self):
        while True:
            print("\n===== Student Registration Menu =====")
            print("1. Register Student")
            print("2. View All Students")
            print("3. Search Student")
            print("4. Delete Student")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.search_student()
            elif choice == "4":
                self.delete_student()
            elif choice == "5":
                print("\nExiting Student Registration System.")
                break
            else:
                print("\nInvalid choice. Please try again.")


# Main Program
if __name__ == "__main__":
    system = StudentRegistrationSystem()
    system.menu()
print("Student Registration System")
print("Student Registration Portal")