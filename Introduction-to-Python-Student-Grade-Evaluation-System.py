total_marks_obtained = float(input("Enter the total marks obtained (out of 500): "))
total_marks = 500

percentage = (total_marks_obtained / total_marks) * 100

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "Fail"

print("Percentage =", percentage, "%")
print("Grade =", grade)
