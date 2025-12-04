# Name: Jerrod Bolton
# Date: Dec 
# Dec 4, 2025
# Python class 235 Programming I - Data Collections
# Assignment 5 - Lists

# I need to add the College info to my program.

college_name = ("University of Advancing Technology ", "Tempe", "901 Baseline Rd.")


# This is the college information and address welcoming message to the student on the program.

print("Hey welcome to", college_name[0])
print("Located in", college_name[1])
print("Address:", college_name[2])
print("=============================================")


# I would like to make a list for college that I need to take this semester. 

def college_courses():
    # List of college courses for the semester
    courses = [
        "Introduction to Programming",
        "Data Structures",
        "Database Management",
        "Web Development",
        "Software Engineering"
    ]

    print("Here is the list of courses you need to take this semester:")
    for index, course in enumerate(courses, start=1):
        print(f"{index}. {course}")

    print("\nGood luck with your studies!")
