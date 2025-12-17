# Jerrod Bolton
# Dec 15. 2025
# Define workout exercises
# Final Project - final project 

# In this proiject, I created a solo level workout generator using the random module also GIU is going to show the generated workout.
# Arm workout, leg workout, and core workout will be generated based on user input.
import random
import tkinter as tk
import time
from tkinter import messagebox
from tkinter import ttk

def welcome_message():
    messagebox.showinfo("Welcome", "Welcome to Solo Leveling Workout Generator! Select a workout type and click 'Generate Workout' to get started.")



# Define workout exercises
def get_a_random_workout_program(exercise_type):
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
    return random.sample(workouts[exercise_type], 3)

def get_time_and_date():
    from datetime import datetime
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

# GUI Applicationns

# Noote: Need the GIU need to show the generated workout opion that a person can choose from arm, leg, or core workout. 
# From that the program will generate a workout based on the user input. 
# The GUI will have a menu to select the workout type and a button to generate the workout
class WorkoutApp:
    def __init__(self, root):  # Constructor to initialize the WorkoutApp class
        self.root = root  # Assign the root window to the class instance   
        self.workout_display = tk.Text(self.root, height=15, width=50) # Create a text box to display the workout
        self.workout_program = []
        self.workout_time = get_time_and_date() # Get the current tiem and date of when workout
        self.workout_display.pack(pady=20) 
        

        # Create the GUI components
        self.create_widgets()  # Call the method to create widgets

    def generate_workout(self): # Method to generate and display the workout
        welcome_message()
        workout_type = self.workout_type.get()
        self.workout_program = get_a_random_workout_program(workout_type)
        self.display_workout()
        self.save_button_appear()  

        
    def display_workout(self): # Method to display the generated workout
        self.workout_display.delete(1.0, tk.END)
        self.workout_display.insert(tk.END, "Workout:\n\n")
        for exercise in self.workout_program:
            self.workout_display.insert(tk.END, f"- {exercise}\n")
            
    def save_workout_data(self): # Method to save workout data to a file
        with open("workout_data.txt", "a") as file:
        # need to get the time and date when the workout was generated and done 
            file.write("Workout Data:")
            file.write("Generated Workout: " + self.workout_time + "\n")
            for exercise in self.workout_program:
                file.write(f"- {exercise}\n")
            file.write("\n")
    
    def save_button_appear(self):
        def show_save_button():
            save_button = ttk.Button(self.root, text="Save Workout", command=self.save_workout_data)
            save_button.pack(pady=10)

        # Set a timer to show the save button after 5 seconds
        self.root.after(40000, show_save_button)
        


    def create_widgets(self): # Method to create GUI components
        self.root.title("Solo Leveling Workout Generator")  # Set the title of the window
        # welcome_message() # Show welcome message like a popup showing welcome to the user
        # Create a frame for the workout selection
        selection_frame = ttk.Frame(self.root, padding="20")
        selection_frame.pack()
        # Create a label for the dropdown menu
        selection_label = ttk.Label(selection_frame, text="Select Workout Type:")
        selection_label.pack()
        # Create a dropdown menu for workout types
        self.workout_type = tk.StringVar()
        workout_options = ["Arm", "Legs", "Core"]
        # Create the dropdown (combobox) widget
        self.workout_dropdown = ttk.Combobox(selection_frame, textvariable=self.workout_type, values=workout_options, state="readonly")
        self.workout_dropdown.pack()
        self.workout_dropdown.current(0)  # Set default selection to the first option
        # Create a button to generate the workout
        generate_button = ttk.Button(self.root, text="Generate Workout", command=self.generate_workout) 
        generate_button.pack(pady=10)
        # Save button will appear after countdown timer
  

        

   
# Create the main window
if __name__ == "__main__":
    root = tk.Tk()  # Initialize the Tkinter root window
    app = WorkoutApp(root)  # Create an instance of the WorkoutApp class
    root.mainloop()  # Start the Tkinter event loop
