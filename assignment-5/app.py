# Name: Jerrod Bolton
# Date: Dec 
# Dec 4, 2025
# Python class 235 Programming I - Data Collections
# Assignment 5 - Lists

registered_courses = []

# this is a list of college courses for the semester that I can take this semester.
list_of_courses = [
        "Introduction to Programming",
        "Data Structures",
        "Database Management",
        "Web Development",
        "Software Engineering", 
        "Computer Networks",
        "Operating Systems",
        "Cybersecurity Fundamentals"
    ]
# lists what the use can do with the program. 
list_of_options = [ 
    "View Available Courses",
    "Register for a Course",
    "View Registered Courses",
    "Drop a Course",
    "exit"
]

# I need to add the College info to my program.
college_name = ("University of Advancing Technology ", "Tempe", "901 Baseline Rd.")

def college_courses():
    # List of college courses for the semester
    print("============================================================================")
    for index, course in enumerate(list_of_courses, start=1):
        print(f"{index}. {course}")

    print("\nGood luck with your studies!")
    print("============================================================================")
    #  if I the keyword global allows me to modify the registered_courses list within the function.
    display_options()
    
def added_course():

    global registered_courses 
    registered_courses = []

    while True:
        course_number = int(input("Enter the number of the course you want to register for (or 0 to stop): "))
        if course_number == 0:
            break
        elif  1 <= course_number <= len(list_of_courses):
            course = list_of_courses[course_number - 1]
            if course not in registered_courses:
                registered_courses.append(course)
                print("============================================================================")
                print(f"You have successfully registered for {course}.")
                print("============================================================================")
                
            else:
                print("You are already registered for this course.")
        else:
            print("Invalid course number. Please try again.")
        
    display_options()
    return registered_courses

def remover_course():
    while True:
        course_number = int(input("Enter the number of the course you want to drop (or 0 to stop): "))
        if course_number == 0:
            break
        elif 1 <= course_number <= len(registered_courses):
            course = registered_courses[course_number - 1]
            registered_courses.remove(course)
            print("============================================================================")
            print(f"You have successfully dropped {course}.")
            print("============================================================================")
        else:
            print("Invalid course number. Please try again.")    
    
    display_options()
    return registered_courses


def view_registered_courses():
    if registered_courses:
        print("You are registered for the following courses:")
        for course in registered_courses:
            print(f" {course}")
    else:
        print("You are not registered for any courses.")
    display_options()


def display_options():

# I would like to make a list for college that I need to take this semester. 
    print("What would like to do today?")
    choice = 0
    while choice < 1 or choice > len(list_of_options):
        for index, option in enumerate(list_of_options, start=1):
            print(f"{index}. {option}")
        choice = int(input("Please enter the number of your choice: "))
        if choice == 1:
            college_courses()
        elif choice == 2:
            added_course()
        elif choice == 3:
            view_registered_courses()
        elif choice == 4:
            remover_course()
        elif choice == 5:
            print("Thank you for using the course registration system. Goodbye!")
        else:
            print("============================================================================")
            print("This feature is not yet implemented. Please choose another option. Or type exit to quit.")
            print("============================================================================")

# This is the college information and address welcoming message to the student on the program.
print("============================================================================")
print("        Hey, Welcome to", college_name[0])
print("        Located in:", college_name[1], "Address:", college_name[2])
print("============================================================================")
print(".       Now let's get you set up for your classes this semester!            ")
# This is calling the display options function to start the program.
display_options()