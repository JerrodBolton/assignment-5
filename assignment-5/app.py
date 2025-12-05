# Name: Jerrod Bolton
# Date: Dec 4, 2025
# Python class 235 Programming I - Data Collections
# Assignment 5 - Lists

# Initialize an empty list to store registered courses
registered_courses = []

# List of college courses available for the semester
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

# List of options for the user to interact with the program
list_of_options = [ 
    "View Available Courses",
    "Register for a Course",
    "View Registered Courses",
    "Drop a Course",
    "exit"
]

# Tuple containing college information (name, city, address)
college_name = ("University of Advancing Technology ", "Tempe", "901 Baseline Rd.")

# Function to display the list of available college courses
def college_courses():
    print("============================================================================")
    # Loop through the list of courses and display each with its index
    for index, course in enumerate(list_of_courses, start=1):
        print(f"{index}. {course}")
    print("\nGood luck with your studies!")
    print("============================================================================")
    # Call the display_options function to show the menu again
    display_options()

# Function to add a course to the registered courses list
def added_course():
    global registered_courses  # Allow modification of the global registered_courses list
    registered_courses = []  # Initialize the registered_courses list

    while True:
        # Prompt the user to enter the course number they want to register for
        course_number = int(input("Enter the number of the course you want to register for (or 0 to stop): "))
        if course_number == 0:  # Exit the loop if the user enters 0
            break
        elif 1 <= course_number <= len(list_of_courses):  # Check if the course number is valid
            course = list_of_courses[course_number - 1]  # Get the course name based on the number
            if course not in registered_courses:  # Check if the course is not already registered
                registered_courses.append(course)  # Add the course to the registered list
                print("============================================================================")
                print(f"You have successfully registered for {course}.")
                print("============================================================================")
            else:
                print("You are already registered for this course.")  # Inform the user if already registered
        else:
            print("Invalid course number. Please try again.")  # Handle invalid course numbers
        
    display_options()  # Call the display_options function to show the menu again
    return registered_courses  # Return the updated registered courses list

# Function to remove a course from the registered courses list
def remover_course():
    while True:
        # Prompt the user to enter the course number they want to drop
        course_number = int(input("Enter the number of the course you want to drop (or 0 to stop): "))
        if course_number == 0:  # Exit the loop if the user enters 0
            break
        elif 1 <= course_number <= len(registered_courses):  # Check if the course number is valid
            course = registered_courses[course_number - 1]  # Get the course name based on the number
            registered_courses.remove(course)  # Remove the course from the registered list
            print("============================================================================")
            print(f"You have successfully dropped {course}.")
            print("============================================================================")
        else:
            print("Invalid course number. Please try again.")  # Handle invalid course numbers
    
    display_options()  # Call the display_options function to show the menu again
    return registered_courses  # Return the updated registered courses list

# Function to view the list of registered courses
def view_registered_courses():
    if registered_courses:  # Check if there are any registered courses
        print("You are registered for the following courses:")
        for course in registered_courses:  # Loop through and display each registered course
            print(f" {course}")
    else:
        print("You are not registered for any courses.")  # Inform the user if no courses are registered
    display_options()  # Call the display_options function to show the menu again

# Function to display the menu options and handle user choices
def display_options():
    print("What would like to do today?")
    choice = 0  # Initialize the user's choice
    while choice < 1 or choice > len(list_of_options):  # Ensure the choice is within valid range
        for index, option in enumerate(list_of_options, start=1):  # Display each option with its index
            print(f"{index}. {option}")
        choice = int(input("Please enter the number of your choice: "))  # Prompt the user for their choice
        if choice == 1:
            college_courses()  # Call the function to display available courses
        elif choice == 2:
            added_course()  # Call the function to register for a course
        elif choice == 3:
            view_registered_courses()  # Call the function to view registered courses
        elif choice == 4:
            remover_course()  # Call the function to drop a course
        elif choice == 5:
            print("Thank you for using the course registration system. Goodbye!")  # Exit message
        else:
            print("============================================================================")
            print("This feature is not yet implemented. Please choose another option. Or type exit to quit.")
            print("============================================================================")

# Display a welcome message with college information
print("============================================================================")
print("        Hey, Welcome to", college_name[0])
print("        Located in:", college_name[1], "Address:", college_name[2])
print("============================================================================")
print(".       Now let's get you set up for your classes this semester!            ")

# Call the display_options function to start the program
display_options()