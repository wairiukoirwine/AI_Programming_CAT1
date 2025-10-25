# student_info_system.py
# Mini Project: AI Student Info System

# Function to save student data to a text file
def save_to_file(students_list):
    with open("students.txt", "w") as file:
        for student in students_list:
            file.write(f"Name: {student['name']}, ID: {student['student_id']}, Favorite AI Tool: {student['favorite_AI_tool']}\n")
    print("\n✅ Student data saved to students.txt successfully!")

# Main program
students = []

print("=== AI Student Info System ===")
while True:
    name = input("Enter student name (or type 'exit' to stop): ")
    if name.lower() == "exit":
        break

    student_id = input("Enter student ID: ")
    favorite_AI_tool = input("Enter favorite AI tool: ")

    # Store each student as a dictionary
    student = {
        "name": name,
        "student_id": student_id,
        "favorite_AI_tool": favorite_AI_tool
    }

    # Add dictionary to the list
    students.append(student)
    print(f"✅ Student {name} added successfully!\n")

# Print summary
print("\n=== Student List Summary ===")
print(f"Total Students: {len(students)}\n")

for i, s in enumerate(students, start=1):
    print(f"{i}. Name: {s['name']}, ID: {s['student_id']}, Favorite AI Tool: {s['favorite_AI_tool']}")

# Save to file
save_to_file(students)

