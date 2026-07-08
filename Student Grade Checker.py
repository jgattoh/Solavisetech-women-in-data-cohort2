#Student Grade Checker

# Write a program that:

# Asks the user for a student's name.
# Asks the user for a score.
# Determines the student's grade:
# 80 and above → A
# 70–79 → B
# 60–69 → C
# Below 60 → F
# Stores the information in a dictionary.
# Stores the student's name in a list.
# Prints a report showing the student's:
# Name
# Score
# Grade
# Rules

# You may only use concepts we've covered:

# Variables
# Strings
# Lists
# Dictionaries
# if, elif, else
# Comparison operators
# append()
# input()
# print()
# Hints (not answers)
# You'll need an empty list somewhere.
# You'll need a dictionary with three pieces of information.
# The grade should be stored in a variable before it goes into the dictionary.
# You'll probably need int() for the score.

Student_name =input("Provide the student's name: ")
Student_score =int(input("Provide the student's score: " ))
if Student_score >= 80:
   grade = "A"
   
elif 70 <= Student_score <= 79:   #or: Student_score >= 70 and Student_score <= 79:
   grade = "B"
   
elif 60 <= Student_score <= 69: #Sor: Student_score >= 60 and Student_score <= 69:
   grade = "C"
   
else: 
   grade = "F"
   

Student_record = {
   "name" :Student_name,
   "score" :Student_score,
   "grade" :grade
}


print (Student_record)