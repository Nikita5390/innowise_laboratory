class StudentManager:
    def __init__(self):
        self.students_list = []

    # add new student in list
    def add_student_name(self, name):
        student = {
            'name': name,
            'grades': list()
        }
        self.students_list.append(student)

    # search student name in list
    def search_student(self, name):
        for student in self.students_list:
            if student["name"] == name:
                return student["grades"]
        return None

    # create new student
    def student_info(self):
        while True:
            try:
                name = str(input("Enter your name: ").strip())
                if not name:
                    print("Please enter a name.")
                    continue
                if not all(ch.isalpha() or ch.isspace() for ch in name):
                    print("Name must contain only letters.")
                    continue

                self.add_student_name(name)
                print("Add student successfully!")
                break

            except KeyboardInterrupt:
                print("Enter interrupt by User!")
                break
            except Exception as e:
                print("Something went wrong.")
                continue

    # add student grade
    def add_grades(self):
        name = str(input("Enter your name: "))
        student_grades = self.search_student(name)
        if student_grades is not None:
            grade_list = []
            while True:
                grades = input("Enter your grades or 'done': ")
                if grades.lower() == "done":
                    break
                try:
                    grades = int(grades)
                    if 0 <= grades <= 100:
                        grade_list.append(grades)
                    else:
                        print("Invalid grades. Enter grades from 0 to 100")
                except ValueError:
                    print("Enter your grades or 'done': ")
            student_grades.extend(grade_list)
            print("Add student grades successfully!")
        else:
            print(f"Student {name} not found!")

    # Report about all students
    def student_report(self):
        print("---Student Report---")
        grades_list = []
        for student in self.students_list:
            try:
                avg_grades = sum(student["grades"]) / len(student["grades"])
                grades_list.append(avg_grades)
                print(f"{student['name']}'s average grade is {round(avg_grades, 1)}")
            except ZeroDivisionError:
                print(f"{student['name']}'s average grade is N/A")
        if grades_list:
            max_avg_grade = max(grades_list)
            min_avg_grade = min(grades_list)
            overall_avg_grade = sum(grades_list) / len(grades_list)
            print("-----------------------------")
            print(f"Max average: {round(max_avg_grade, 1)}")
            print(f"Min average: {round(min_avg_grade, 1)}")
            print(f"Overall average: {round(overall_avg_grade, 1)}")
        else:
            print("No student grades found!")

    # Search the best student in students list with max avg. grade
    def search_best_student(self):
        avg_grades_list = []
        for student in self.students_list:
            name = student['name']
            try:
                avg_grades = sum(student["grades"]) / len(student["grades"])
                info = {
                    "name": name,
                    "avg_grades": avg_grades,
                }
                avg_grades_list.append(info)
            except ZeroDivisionError:
                print(f"Student {name} have N/A grade!")
            except KeyError:
                print("Invalid data structure.")

        if avg_grades_list:
            best_student = max(avg_grades_list, key=lambda x: x["avg_grades"])
            print(
                f"The student with the highest average is {best_student['name']} with a grade of {round(best_student['avg_grades'], 1)}.")
        else:
            print("No students with grades found.")


class Analyzer(object):
    def __init__(self):
        self.manager = StudentManager()

    def menu() -> str:
        return (
                '--- Student Grade Analyzer ---' + '\n'
                                                   '1. Add a new student\n' +
                '2. Add grades for a student\n' +
                '3. Generate a full report\n' +
                '4. Find the top student\n' +
                '5. Exit program\n'
        )

    def make_choice(self, choice: int):
        if choice == 1:
            return self.manager.student_info()
        elif choice == 2:
            return self.manager.add_grades()
        elif choice == 3:
            return self.manager.student_report()
        elif choice == 4:
            return self.manager.search_best_student()
        elif choice == 5:
            return print("Exiting program.")
        else:
            return print("Invalid choice.")


def run() -> None:
    analyzer = Analyzer()
    choice = None
    while choice != 5:
        print(Analyzer.menu())
        try:
            choice = int(input('Enter your choice: '))
            if 1 <= choice > 5:
                print("Please enter a number from 1 to 5!")
                continue
            analyzer.make_choice(choice)

        except ValueError:
            print("Enter integer numbers from 1 to 5!")


run()
