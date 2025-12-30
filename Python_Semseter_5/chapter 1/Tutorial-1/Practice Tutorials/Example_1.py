"""
Exercise 1:
# Create variables
name = "Krishna"
age = 28
grades = [85, 90, 78]
# Print a formatted message using f-string
print(f"{name} is {age} years old and scored {grades[1]} in the test.")
"""

name =input("Enter name: ")
age = int(input("Enter age: "))
subjects=int(input("Enter number of subjects: "))
grades=[]

for i in range(subjects):
    print(f"Enter marks of {i+1}th subject: " ,end=" ")
    a=int(input())
    grades.append(a)

print(f"{name} is {age} years old and scored following marks in test:")
for i in range(subjects):
    print(f"{grades[i]} in {i+1}th subject")
