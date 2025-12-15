# ======================================================================================================================================
# Author: Jerrod Bolton
# Date: December 10, 2024
# Assignment 7: Data Loading and Formatting with Pandas
#
# Description:
# This program demonstrates how to load a large CSV dataset using the pandas library,
# format the column names for readability, and display a preview of the formatted data
# in the terminal. This assignment focuses on reading large datasets and using at least
# one external Python package.
# ======================================================================================================================================

# Import the pandas library
# Pandas is used for reading, manipulating, and analyzing structured data such as CSV files
import pandas as pd
def load_dataset(the_file_name):
    # Loads a CSV dataset into a pandas DataFrame.
    # Parameters:
    #     the_file_name (str): The name of the CSV file to load.
    # Returns:
    #     pd.DataFrame: A DataFrame containing the loaded dataset.
    # Read the CSV file and store it in a pandas DataFrame
    # Pandas automatically parses the CSV into rows and columns
    data = pd.read_csv(the_file_name)

    # Print a confirmation message so the user knows the file was loaded successfully
    print(f"[INFO] Loaded dataset from '{the_file_name}'.")

    # Return the DataFrame to be used elsewhere in the program
    return data


def format_dataset(df):
    # Renames dataset columns to make them more readable and consistent.
    # Parameters:
    #     df (pd.DataFrame): The original dataset.
    # Returns:
    #     pd.DataFrame: The formatted dataset with updated column names.
    # Rename columns using a dictionary mapping
    # This improves readability and makes column names more Python-friendly
    df = df.rename(
        columns={
            "work_year": "WorkYear",
            "experience_level": "ExperienceLevel",
            "employment_type": "EmploymentType",
            "job_title": "JobTitle",
            "salary": "Salary",
            "salary_currency": "SalaryCurrency",
            "salary_in_usd": "SalaryInUSD",
            "employee_residence": "EmployeeResidence",
            "remote_ratio": "RemoteRatio",
            "company_location": "CompanyLocation",
            "company_size": "CompanySize",
        }
    )

    # Return the modified DataFrame
    return df


def display_results(df):
    # Displays the first 10 rows of the formatted dataset in the terminal.
    # Parameters:
    #     df (pd.DataFrame): The formatted dataset to display.

    # Print a separator line for better terminal readability
    print("==============================================")
    # Inform the user what data is being displayed
    print("First 10 rows of the formatted dataset:")

    # Display the first 10 rows of the DataFrame
    # head(10) ensures we do not overwhelm the terminal with data
    print(df.head(5))
    # Print another separator line to visually close the output
    print("==============================================") 
    
    print("\n[INFO] Data display complete.")  # Inform the user that data display is complete
    print("==============================================")
    


# ======================================================================================================================================
# Program Entry Point
# This block ensures the code below only runs when this file is executed directly
# and not when it is imported as a module.
# ======================================================================================================================================
if __name__ == "__main__":
    # Specify the CSV file name to be loaded
    file_name = "salaries.csv"
    # Load the dataset from the CSV file
    df = load_dataset(file_name)
    # Format the dataset by renaming columns
    df = format_dataset(df)
    # Display the formatted results in the terminal
    display_results(df)
