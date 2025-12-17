# Solo Leveling Workout Generator (Final Project)

## Overview
**Solo Leveling Workout Generator** is a beginner-friendly fitness game built in Python.  
It lets a user choose what body area they want to train (like **Arms**, **Legs**, or **Core**) and then the app randomly selects an exercise for them to complete — like a “quest” from a Solo Leveling-style training system.

The goal is to make working out feel like a game: pick a category, get a challenge, and level up your discipline.

---

## What This App Does
- Displays an opening screen with instructions
- Lets the user choose a workout category:
  - **Arms**
  - **Legs**
  - **Core**
  - (Optional: Full Body / Cardio)
- Randomly generates an exercise “challenge” from that category
- Shows the chosen exercise on the screen (GUI)
- Lets the user generate another exercise or exit

---

## How To Use (For First-Time Users)
1. Open the application.
2. Read the instructions on the opening screen.
3. Choose the body area you want to train (ex: Arms).
4. Click **Generate Workout** (or choose from menu buttons).
5. The app will display a random exercise challenge.
6. Click **Generate Again** to get a new one, or **Exit** to stop.

---

## Example Exercises (Sample)
**Arms**
- Push-ups (standard or knee)
- Tricep dips (chair)
- Bicep curls (if weights available)
- Plank shoulder taps

**Legs**
- Squats
- Lunges
- Wall sit
- Calf raises

**Core**
- Plank
- Crunches
- Bicycle kicks
- Leg raises

---

## Project Requirements Checklist (Rubric Alignment)
This project is designed to meet the course requirements:

- ✅ **Opening screen** with app description and instructions  
- ✅ **User input** (user chooses workout category + buttons/menu choices)  
- ✅ **Output to display** (shows the randomly generated exercise)  
- ✅ **Variables** using multiple data types (strings, integers, booleans, lists)  
- ✅ **Menu choices** (GUI buttons OR command-style options)  
- ✅ **10+ functions** (see planned functions below)  
- ✅ Uses at least one data collection type: **List / Dictionary**  
- ✅ Uses a program loop: **while loop** (or event loop in GUI)  
- ✅ Uses a Python library: **random** (to generate exercises)  

---

## Planned Functions (Function Map)
Below is the planned function layout for the app (before coding):

1. `show_opening_screen()`  
   - Displays the title + instructions to the user.

2. `build_exercise_database()`  
   - Creates and returns the list/dictionary of exercises by category.

3. `create_main_window()`  
   - Sets up the GUI window, title, and layout.

4. `create_menu_buttons()`  
   - Creates buttons for Arms / Legs / Core (and any extras).

5. `handle_category_selection(category)`  
   - Runs when user selects a category (ex: Arms).

6. `get_random_exercise(category, database)`  
   - Uses the `random` library to return one random exercise from the chosen category.

7. `display_exercise(exercise)`  
   - Displays the selected exercise on the screen.

8. `generate_again()`  
   - Generates a new random exercise using the last selected category.

9. `reset_session()`  
   - Clears text/output and returns app to the selection menu.

10. `exit_app()`  
   - Safely closes the application.

*(Optional Bonus Functions)*  
11. `track_completed_workouts()`  
12. `show_stats()` (ex: “You generated 5 arm workouts today!”)

---

## Python Library Used
- **random**  
  - Used to choose a random workout exercise from the selected category.

(Optional but useful later)
- `datetime` (if you want to track the day/time of workouts)

---

## Files Included
- `app.py` (main program)
- Any images/sounds you add (optional)

---

## Demo Video (YouTube)
A short demo video (under 5 minutes) will show:
1. Opening screen & instructions  
2. Selecting a category (Arms/Legs/Core)  
3. Generating random exercises  
4. Generating again / resetting  
5. Exiting the program  

**YouTube Link:** *(add link here once uploaded)*

---

## Future Improvements (Optional Ideas)
- Add difficulty levels (Beginner / Intermediate / Advanced)
- Add “leveling system” with XP points
- Add timers for exercises (ex: 30-second plank)
- Add a full-body “Daily Dungeon” mode

---

## Author
Jerrod Bolton  
Final Project — Python Course
