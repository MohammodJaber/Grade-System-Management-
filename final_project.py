import csv

# Function to add student details
def add_student():
    name = input("Enter Student Name: ")
    
    student_id = input("Enter Student ID: ")
    grade = float(input("Enter Grade (0-100): "))
    with open("students.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, student_id, grade])
    print(f"Student {name} added successfully!\n")

# Function to view all student records
def view_students():
    try:
        with open("students.csv", "r") as file:
            reader = csv.reader(file)
            print("\n--- Student Records ---")
            print(f"{'Name':<15}{'ID':<10}{'Grade':<10}")
            print("-" * 35)
            for row in reader:
                print(f"{row[0]:<15}{row[1]:<10}{row[2]:<10}")
    except FileNotFoundError:
        print("No student records found. Please add students first.\n")

# Function to analyze grades
def analyze_grades():
    try:
        grades = []
        with open("students.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                grades.append(float(row[2]))

        if grades:
            print("\n--- Grade Analysis ---")
            print(f"Average Grade: {sum(grades) / len(grades):.2f}")
            print(f"Highest Grade: {max(grades)}")
            print(f"Lowest Grade: {min(grades)}\n")
        else:
            print("No grades available for analysis.\n")
    except FileNotFoundError:
        print("No student records found. Please add students first.\n")

# Main menu
def main():
    while True:
        print("\n--- Student Grade Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Analyze Grades")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            analyze_grades()
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
if __name__ == "__main__":
    main()
    