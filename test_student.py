def student_details(name, student_id, department, marks):
    return {
        "Student Name": name,
        "Student ID": student_id,
        "Department": department,
        "Marks": marks
    }


if __name__ == "__main__":
    details = student_details("Alice", "S1001", "Computer Science", 85)
    print(details)
