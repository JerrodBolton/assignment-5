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
        "Incline Push-ups - 3 sets of 12 reps",
        "Knee Push-ups - 3 sets of 10 reps",
        "Bicep Curls - 3 sets of 12 reps",
        "Hammer Curls - 3 sets of 12 reps",
        "Tricep Dips - 3 sets of 15 reps",
        "Overhead Tricep Extension - 3 sets of 12 reps",
        "Shoulder Press - 3 sets of 12 reps",
        "Lateral Raises - 3 sets of 12 reps",
        "Arm Circles - 3 sets of 30 seconds"
    ],

    "Legs": [
        "Squats - 3 sets of 15 reps",
        "Jump Squats - 3 sets of 10 reps",
        "Lunges - 3 sets of 12 reps each leg",
        "Reverse Lunges - 3 sets of 10 reps each leg",
        "Step-Ups - 3 sets of 12 reps each leg",
        "Glute Bridges - 3 sets of 15 reps",
        "Wall Sit - Hold for 30 seconds, 3 times",
        "Calf Raises - 3 sets of 20 reps",
        "Single-Leg Calf Raises - 3 sets of 12 reps each leg",
        "High Knees - 3 sets of 30 seconds"
    ],

    "Core": [
        "Crunches - 3 sets of 20 reps",
        "Sit-Ups - 3 sets of 15 reps",
        "Leg Raises - 3 sets of 15 reps",
        "Flutter Kicks - 3 sets of 20 reps",
        "Russian Twists - 3 sets of 20 reps",
        "Bicycle Crunches - 3 sets of 20 reps",
        "Plank - Hold for 1 minute, 3 times",
        "Side Plank - Hold for 30 seconds each side",
        "Mountain Climbers - 3 sets of 30 seconds",
        "Toe Touches - 3 sets of 20 reps"
    ],

    "Cardio": [
        "Jumping Jacks - 3 sets of 30 seconds",
        "High Knees - 3 sets of 30 seconds",
        "Butt Kicks - 3 sets of 30 seconds",
        "Jog in Place - 3 sets of 1 minute",
        "Burpees - 3 sets of 8 reps",
        "Skater Jumps - 3 sets of 20 reps",
        "Jump Rope (Imaginary) - 3 sets of 1 minute",
        "Mountain Climbers - 3 sets of 30 seconds",
        "Fast Marching - 3 sets of 1 minute",
        "Shadow Boxing - 3 sets of 1 minute"
    ],

    "Full Body": [
        "Burpees - 3 sets of 10 reps",
        "Push-up to Squat - 3 sets of 10 reps",
        "Squat to Press - 3 sets of 12 reps",
        "Mountain Climbers - 3 sets of 30 seconds",
        "Bear Crawl - 3 sets of 30 seconds",
        "Plank Jacks - 3 sets of 20 reps",
        "Jump Squats - 3 sets of 10 reps",
        "Dead Bug - 3 sets of 10 reps each side",
        "Standing Knee Raises - 3 sets of 20 reps",
        "Lunge to Knee Drive - 3 sets of 10 reps each leg"
    ],

    "HIIT": [
        "Jump Squats - 3 sets of 12 reps",
        "Burpees - 3 sets of 8 reps",
        "High Knees - 3 sets of 30 seconds",
        "Mountain Climbers - 3 sets of 30 seconds",
        "Skater Jumps - 3 sets of 20 reps",
        "Plank Jacks - 3 sets of 20 reps",
        "Speed Squats - 3 sets of 15 reps",
        "Fast Feet Shuffle - 3 sets of 30 seconds",
        "Jump Lunges - 3 sets of 10 reps",
        "Power Knees - 3 sets of 20 reps"
    ],

    "Mobility": [
        "Arm Swings - 3 sets of 30 seconds",
        "Hip Circles - 3 sets of 30 seconds",
        "Torso Twists - 3 sets of 30 seconds",
        "Cat-Cow Stretch - 3 sets of 10 reps",
        "World’s Greatest Stretch - Hold for 30 seconds each side",
        "Neck Rolls - 3 sets of 20 seconds",
        "Shoulder Rolls - 3 sets of 30 seconds",
        "Ankle Circles - 3 sets of 30 seconds",
        "Standing Forward Fold - Hold for 1 minute",
        "Chest Opener Stretch - Hold for 30 seconds"
    ],

    "Recovery": [
        "Light Walking - 5 minutes",
        "Deep Breathing - 3 minutes",
        "Child’s Pose - Hold for 1 minute",
        "Seated Forward Fold - Hold for 1 minute",
        "Standing Hamstring Stretch - Hold for 30 seconds each leg",
        "Quad Stretch - Hold for 30 seconds each leg",
        "Shoulder Stretch - Hold for 30 seconds each arm",
        "Calf Stretch - Hold for 30 seconds each leg",
        "Neck Stretch - Hold for 30 seconds each side",
        "Supine Twist - Hold for 1 minute each side"
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
        self.save_button = None  # Initialize the save button as None
        self.timer_label = ttk.Label(self.root, text="")
        self.timer_label.pack(pady=5)

        # Create the GUI components
        self.create_widgets()  # Call the method to create widgets

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
            file.write("\n") # Add a newline
        print("---------------------------------------------------------------------------------------")  # Print a separator
        print("Workout data saved successfully.")  # Print a success message
        print(f"Hey {input_name}, your workout data saved to workout_data.txt at: {self.workout_time}")  # Print a confirmation message
        print("---------------------------------------------------------------------------------------")  # Print a separator
        

     # Method to show the save button after a delay
    # def save_button_appear(self):
    #     def show_save_button():
    #         save_button = ttk.Button(self.root, text="Save Workout", command=self.save_workout_data)  # Create the save button
    #         save_button.pack(pady=10)  # Add padding around the button
    #     def hide_save_button_forget():
    #         hide_save_button.pack_forget()  # Hide the save button

    #     def hide_save_button():
    #     hide_save_button = ttk.Button(self.root, text="Save Workout", command=hide_save_button())  # Create the save button
    #     hide_save_button.pack(pady=10)  # Add padding around the button

         # self.root.after(100000, show_save_button)  # Show the save button after 1 second
         # self.root.after(190000, hide_save_button)  # Hide the save button after 1.9 seconds
    #     self.root.after(1000, show_save_button)  # Show the save button after 1 second
    #     self.root.after(1900, hide_save_button)  # Hide the save button after 1.9 seconds

    def save_button_appear(self):
        def show_save_button():
            self.save_button = ttk.Button(
                self.root,
                text="Save Workout",
                command=self.save_workout_data
            )
            self.save_button.pack(pady=10)

            # Schedule the button to disappear after 10 seconds
            self.root.after(10000, hide_save_button)

        def hide_save_button():
            if self.save_button:
                self.save_button.destroy()
                self.save_button = None
                    
    # Show the save button after 30 seconds
        self.root.after(45000, show_save_button)

    # def countdown(self):
    #         if self.timer > 0:
    #             mins, secs = divmod(self.timer, 60)
    #             time_format = f"{mins:02d}:{secs:02d}"
    #             self.timer_label.config(
    #                 text=f"Time remaining to save workout: {time_format}"
    #             )
    #             self.timer -= 1
    #             self.root.after(1000, self.countdown)  # call again in 1 second
    #         else:
    #             self.timer_label.config(text="Time is up!")

    # Method to generate and display the workout
    def generate_workout(self):
        workout_type = self.workout_type.get()  # Get the selected workout type from the dropdown
        self.workout_program = get_a_random_workout_program(workout_type)  # Generate a random workout program
        self.display_workout()  # Display the generated workout
        self.timer = 30  # countdown time in seconds
        # input_user_data()  # Call the function to input user data
        # self.countdown()  # Start the countdown timer
        self.save_button_appear()  # Show the save button after a delay
    

    # Method to create GUI components
    def create_widgets(self):
        self.root.title("Solo Leveling Workout Generator")  # Set the title of the window
        # Create a description label
        description_label = ttk.Label(
            self.root,
            text=(
                "Solo Leveling Workout Generator\n\n"
                "Choose a workout type below and click 'Generate Workout'.\n"
                "You will receive a random exercise challenge.\n"
                "Complete the workout and save your progress to level up!\n" 
                f"The save button will appear after 3 minutes to log your workout.\n\n"
                "Good luck, and have fun working out!!!!"
                
            ),
            justify="center",
            wraplength=400
        )
        description_label.pack(pady=10) # Add padding around the description label
        # Create a frame for the workout selection
        selection_frame = ttk.Frame(self.root, padding="20")  # Create a frame with padding
        selection_frame.pack()  # Add the frame to the window

        # Create a label for the dropdown menu
        selection_label = ttk.Label(selection_frame, text="Select Workout Type:")  # Create a label
        selection_label.pack()  # Add the label to the frame

        # Create a dropdown menu for workout types
        self.workout_type = tk.StringVar()  # Create a StringVar to hold the selected workout type
        workout_options = [
        "Arm", "Legs", "Core",
        "Cardio", "Full Body",
        "HIIT", "Mobility", "Recovery"
        ]  
        # Define the workout options
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

