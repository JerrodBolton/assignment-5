#  This is a simple Tkinter GUI application that displays "Hello World!" and has a button to quit the application.
# ------------------------------------------------------------------------------------
# from tkinter import *
# from tkinter import ttk
# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm,
# text="Quit", command=root.destroy).grid(column=1, row=0)
# start the GUI event loop
# root.mainloop()
# ------------------------------------------------------------------------------------

# Jerrod Bolton
# Date: Dec 5, 2025
# Python Class 235 Programming I - Assignment 

# Lesson 6: Introduction to Python - Create a GUI

# For the assignment, create a simple GUI application using Tkinter that displays information about different people that I may in my contact list. When I choose a person from the list and click a button, their information (name, phone number, email) should be displayed in the GUI
import tkinter as tk  # Import the tkinter module for GUI creation
from tkinter import ttk  # Import ttk for themed widgets

class ContactApp:
    def __init__(self, root):
        self.root = root  # Set the root window
        self.root.title("Contact List")  # Set the title of the window
        
        # Contact data dictionary containing name, phone, and email
        self.contact_data = {
            "Jerrod": {"name": "Jerrod", 
                       "phone": "901-555-5678",
                       "email": "JerrodBolton2000@gmail.com"},
            "Alice": {"name": "Alice",
                      "phone": "901-555-1232",
                      "email": "alice@love.com"},
            "Bob": {"name": "Bob",
                    "phone": "901-555-8765",
                    "email": "Boblove@gmail.com"}
        }
        
        # Create the GUI components
        self.create_widgets()
    
    def create_widgets(self):
        # Create a frame for the listbox
        listbox_frame = ttk.Frame(self.root, padding="20")
        listbox_frame.pack()  # Pack the frame into the window
        
        # Create a label for the listbox
        listbox_label = ttk.Label(listbox_frame, text="Select a Contact:")
        listbox_label.pack()  # Pack the label into the frame
        
        # Create a listbox to display contact names
        self.contact_listbox = tk.Listbox(listbox_frame, width=20, height=10)
        self.contact_listbox.pack()  # Pack the listbox into the frame
        
        # Add contact names to the listbox
        for contact in self.contact_data.values():
            self.contact_listbox.insert(tk.END, contact["name"])  # Insert each contact name into the listbox
        
        # Create a frame for the information display
        info_frame = ttk.Frame(self.root, padding="20")
        info_frame.pack()  # Pack the frame into the window
        
        # Create a label to display contact information
        self.info_label = ttk.Label(info_frame, text="", font=("Arial", 12))
        self.info_label.pack()  # Pack the label into the frame
        
        # Create a button frame
        button_frame = ttk.Frame(self.root, padding="20")
        button_frame.pack()  # Pack the frame into the window
        
        # Create a button to show selected contact's information
        button = ttk.Button(button_frame, text="Show Info", command=self.button_click)
        button.pack()  # Pack the button into the frame
    
    def display_contact(self, contact):
        # Extract contact details
        name = contact["name"]
        phone = contact["phone"]
        email = contact["email"]
        
        # Format the contact information as a string
        info_text = f"Name: {name}\nPhone: {phone}\nEmail: {email}"
        # Update the label to display the contact information
        self.info_label.config(text=info_text)
    
    def button_click(self):
        # Get the selected contact from the listbox
        selected_contact = self.contact_listbox.get(tk.ACTIVE)
        # If the selected contact exists in the contact data, display their information
        if selected_contact in self.contact_data:
            self.display_contact(self.contact_data[selected_contact])

# Create the main window
if __name__ == "__main__":
    root = tk.Tk()  # Initialize the Tkinter root window
    app = ContactApp(root)  # Create an instance of the ContactApp class
    root.mainloop()  # Start the Tkinter event loop
