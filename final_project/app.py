# Jerrod Bolton
# Dec 15, 2025
# Define workout exercises
# Final Project - final project

# In this project, I created a solo level workout generator using the random module. 
# The GUI will show the generated workout. Arm workout, leg workout, and core workout will be generated based on user input.

import random  # Import the random module for generating random workouts
import tkinter as tk  # Import tkinter for GUI development
import time  # Import time module (though not used in the code)
from tkinter import messagebox  # Import messagebox for displaying pop-up messages
from tkinter import ttk  # Import ttk for themed widgets


# this get the user name
input_name = input("Enter your name: ")
# Function to display a welcome message in a pop-up window
def welcome_message():
    messagebox.showinfo("Welcome", f"Welcome to the Solo Leveling Workout Generator, {input_name}! Let's get started!")
# Function to get a random workout program based on the selected exercise type
def get_a_random_workout_program(exercise_type):
    # Dictionary containing workout exercises for each type
    workouts = {
        "Arm": [
            "Push-ups - 3 sets of 15 reps",
            "Bicep Curls - 3 sets of 12 reps",
            "Tricep Dips - 3 sets of 15 reps",
            "Shoulder Press - 3 sets of 12 reps",
            "Plank to Push-up - 3 sets of 10 reps"
        ],
        "Legs": [
            "Squats - 3 sets of 15 reps",
            "Lunges - 3 sets of 12 reps each leg",
            "Calf Raises - 3 sets of 20 reps",
            "Glute Bridges - 3 sets of 15 reps",
            "Wall Sit - Hold for 30 seconds, 3 times"
        ],
        "Core": [
            "Crunches - 3 sets of 20 reps",
            "Leg Raises - 3 sets of 15 reps",
            "Russian Twists - 3 sets of 20 reps",
            "Plank - Hold for 1 minute, 3 times",
            "Bicycle Crunches - 3 sets of 20 reps"
        ]
    }
    # Return 3 random exercises from the selected workout type
    return random.sample(workouts[exercise_type], 3)

# Function to get the current date and time
def get_time_and_date():
    from datetime import datetime  # Import datetime module
    now = datetime.now()  # Get the current date and time
    return now.strftime("%Y-%m-%d %H:%M:%S")  # Format the date and time as a string

# GUI Application class
class WorkoutApp:
    def __init__(self, root):  # Constructor to initialize the WorkoutApp class
        self.root = root  # Assign the root window to the class instance
        self.workout_display = tk.Text(self.root, height=15, width=50)  # Create a text box to display the workout
        self.workout_program = []  # Initialize an empty list to store the workout program
        self.workout_time = get_time_and_date()  # Get the current time and date
        self.workout_display.pack(pady=20)  # Add padding around the text box

        # Create the GUI components
        self.create_widgets()  # Call the method to create widgets

    # Method to generate and display the workout
    def generate_workout(self):
        workout_type = self.workout_type.get()  # Get the selected workout type from the dropdown
        self.workout_program = get_a_random_workout_program(workout_type)  # Generate a random workout program
        self.display_workout()  # Display the generated workout
        # input_user_data()  # Call the function to input user data
        self.save_button_appear()  # Show the save button after a delay

    # Method to display the generated workout
    def display_workout(self):
        self.workout_display.delete(1.0, tk.END)  # Clear the text box
        self.workout_display.insert(tk.END, "Workout:\n\n")  # Add a header
        for exercise in self.workout_program:  # Loop through the workout program
            self.workout_display.insert(tk.END, f"- {exercise}\n")  # Display each exercise

    # Method to save workout data to a file
    def save_workout_data(self):
        with open("workout_data.txt", "a") as file:  # Open the file in append mode
            file.write("Workout Data:\n")  # Write a header
            file.write("Generated Workout: " + self.workout_time + "\n")  # Write the date and time
            for exercise in self.workout_program:  # Loop through the workout program
                file.write(f"- {exercise}\n")  # Write each exercise
            file.write("\n")  # Add a newline

    # Method to show the save button after a delay
    def save_button_appear(self):
        def show_save_button():
            save_button = ttk.Button(self.root, text="Save Workout", command=self.save_workout_data)  # Create the save button
            save_button.pack(pady=10)  # Add padding around the button

        # Set a timer to show the save button after 40 seconds
        self.root.after(40000, show_save_button)

    # Method to create GUI components
    def create_widgets(self):
        self.root.title("Solo Leveling Workout Generator")  # Set the title of the window

        # Create a frame for the workout selection
        selection_frame = ttk.Frame(self.root, padding="20")  # Create a frame with padding
        selection_frame.pack()  # Add the frame to the window

        # Create a label for the dropdown menu
        selection_label = ttk.Label(selection_frame, text="Select Workout Type:")  # Create a label
        selection_label.pack()  # Add the label to the frame

        # Create a dropdown menu for workout types
        self.workout_type = tk.StringVar()  # Create a StringVar to hold the selected workout type
        workout_options = ["Arm", "Legs", "Core"]  # Define the workout options
        self.workout_dropdown = ttk.Combobox(selection_frame, textvariable=self.workout_type, values=workout_options, state="readonly")  # Create the dropdown
        self.workout_dropdown.pack()  # Add the dropdown to the frame
        self.workout_dropdown.current(0)  # Set the default selection to the first option

        # Create a button to generate the workout
        generate_button = ttk.Button(self.root, text="Generate Workout", command=self.generate_workout)  # Create the generate button
        generate_button.pack(pady=10)  # Add padding around the button

# Create the main window
if __name__ == "__main__": 
    welcome_message()
    root = tk.Tk()  # Initialize the Tkinter root window
    app = WorkoutApp(root)  # Create an instance of the WorkoutApp class
    root.mainloop()  # Start the Tkinter event loop
     # Show the welcome message

