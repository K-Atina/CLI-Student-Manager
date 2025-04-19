import sys
import time


class Student:
    def __init__(self, name, student_id, mark):
        self.name = name
        self.student_id = student_id
        self.__mark = mark
        
    def introduce(self):
        print(f"Student name: {self.name}, Student ID: {self.student_id}")
        print(f"Grade: {self.__mark}")
    
    def get_mark(self):
        return self.__mark
    
    def set_mark(self, mark):
        if mark < 0:
            raise ValueError("Grade cannot be negative!")
        self.__mark = mark
        
    def is_passing(self):
        passing = self.__mark >= 50
        print("PASS!" if passing else "FAIL!")
        return passing


class ScholarshipStudent(Student):
    def __init__(self, name, student_id, mark, scholarship_amount):
        super().__init__(name, student_id, mark)
        self.__scholarship_amount = scholarship_amount
  
    def get_scholarship_amount(self):
        return self.__scholarship_amount
    
    def set_scholarship_amount(self, scholarship_amount):
        if scholarship_amount < 0:
            raise ValueError("Scholarship amount cannot be negative!")
        self.__scholarship_amount = scholarship_amount
    
    def introduce(self):
        super().introduce()
        print(f"Scholarship Amount: ${self.__scholarship_amount}")

def type_out(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print() 

def exit_program():
    time.sleep(1)
    print("Thank you for working with us")
    time.sleep(0.5)
    print("Bye!")
    sys.exit()

def main():
    type_out("\nWelcome to student manager!")
    time.sleep(1)
    
  
    students = []
    
    while True:
        type_out("\n===== MENU =====")
        time.sleep(0.5)
        type_out("1. Add Regular Student")
        time.sleep(0.5)
        type_out("2. Add Scholarship Student")
        time.sleep(0.5)
        type_out("3. View all Students")
        time.sleep(0.5)
        type_out("4. Update Student Grade")
        time.sleep(0.5)
        type_out("5. Exit")
        time.sleep(0.5)
        
        type_out("Enter your choice: ")
        
        choice = input()
        
        if choice == "1":
            try:
                name = input("Enter student name: ")
                student_id = int(input("Enter Student ID: "))
                mark = int(input("Enter student mark: "))
                
                if not name.strip():
                    print("Name cannot be empty!")
                    continue
                
                
                if any(student.student_id == student_id for student in students):
                    print("Error: A student with this ID already exists!")
                    continue
                    
                new_student = Student(name, student_id, mark)
                students.append(new_student)
                print("\nStudent added successfully!")
                new_student.introduce()
                new_student.is_passing()
                
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "2":
            try:
                name = input("Enter student name: ")
                student_id = int(input("Enter Student ID: "))
                mark = int(input("Enter student mark: "))
                scholarship_amount = int(input("Enter Scholarship Amount: $"))
                
                if not name.strip():
                    print("Name cannot be empty!")
                    continue
                
               
                if any(student.student_id == student_id for student in students):
                    print("Error: A student with this ID already exists!")
                    continue
                    
                new_student = ScholarshipStudent(name, student_id, mark, scholarship_amount)
                students.append(new_student)
                print("\nScholarship Student added successfully!")
                new_student.introduce()
                new_student.is_passing()
                
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "3":
            if not students:
                print("No students registered yet.")
            else:
                print("\n----- All Students -----")
                for i, student in enumerate(students, 1):
                    print(f"\nStudent {i}:")
                    student.introduce()
                    student.is_passing()
        
        elif choice == "4":
            if not students:
                print("No students registered yet.")
                continue
                
            try:
                student_id = int(input("Enter Student ID to update: "))
                
                
                found = False
                for student in students:
                    if student.student_id == student_id:
                        found = True
                        new_mark = int(input("Enter new grade: "))
                        student.set_mark(new_mark)
                        print("Grade updated successfully!")
                        student.introduce()
                        student.is_passing()
                        break
                
                if not found:
                    print("No student found with that ID.")
                    
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "5":
            exit_program()
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()