# LMS system using Python classes and objects

class Student:
    def __init__(self, email="", name=""):
        self.email = email
        self.name = name
        self.registered_courses = []
        self.logged_in = False  # Track login status

    def login(self, email, name):
        self.email = email
        self.name = name
        self.logged_in = True
        print(f"Welcome {self.name}! You are now logged in.")

    def logout(self):
        print("You have been logged out. Goodbye!")
        self.logged_in = False
        return True  # signal to break main loop

    def register_course(self, course_list):
        print("\nAvailable Courses:")
        for idx, course in enumerate(course_list, start=1):
            print(f"{idx}. {course}")
        
        try:
            choice = int(input("Enter the number of the course you want to register: "))
            if 1 <= choice <= len(course_list):
                selected_course = course_list[choice - 1]
                if selected_course not in self.registered_courses:
                    self.registered_courses.append(selected_course)
                    print(f"\nThank you! You have successfully registered for '{selected_course}'.\n")
                else:
                    print("\nYou have already registered for this course.\n")
            else:
                print("Invalid course number selected.")
        except ValueError:
            print("Please enter a valid number.")

class LMS:
    def __init__(self):
        self.courses = ["Mathematics", "Physics", "Computer Science", "Cybersecurity", "IoT"]
        self.student = Student()

    def run(self):
        while True:
            print("\n===== LMS Menu =====")
            if not self.student.logged_in:
                print("1. Login")
                print("2. Exit")
            else:
                print("1. Register a Course")
                print("2. Logout")

            try:
                choice = int(input("Select an option: "))

                if not self.student.logged_in:
                    match choice:
                        case 1:
                            email = input("Enter your email to login: ")
                            name = input("Enter your name: ")
                            self.student.login(email, name)
                        case 2:
                            print("Goodbye!")
                            break
                        case _:
                            print("Invalid option. Please choose between 1 and 2.")
                else:
                    match choice:
                        case 1:
                            self.student.register_course(self.courses)
                        case 2:
                            if self.student.logout():
                                break
                        case _:
                            print("Invalid option. Please choose between 1 and 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")

# Run the LMS system
if __name__ == "__main__":
    lms = LMS()
    lms.run()
