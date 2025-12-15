# Assignment 7 Overview

In this assignment, we will learn how to **write and read large datasets**. You must also use **at least one Python package** in your program.

## Guidelines
- Use an existing large dataset or create a large dataset/file.
- Read that dataset and apply some formatting to the data.

## Expectations
1. Find or create a large file.
2. Read that large file.
3. Format the data in some way and display the data (using the package you included).
4. Over-comment your source code file (`.py`) well.
5. Each program should have a great user experience.

## Deliverables / Submission
- Source code: `.py` file for your application
- Screenshot(s) or a YouTube link to a video of your app running
- Do **not** zip the submission

---

# About the Dataset

This dataset contains salary information from **ai-jobs**, which collects salary data anonymously from professionals worldwide in **AI/ML and Big Data** and makes it publicly available. The dataset is updated regularly, typically **weekly**, as new submissions come in.

**Primary goal:** provide better guidance on what professionals are being paid globally.

---

# Dataset Fields

The dataset contains one table with the following fields:

## Column Definitions

- **work_year**: The year the salary was paid.

- **experience_level**: The experience level during the work year.
  - **EN**: Entry-level / Junior  
  - **MI**: Mid-level / Intermediate  
  - **SE**: Senior-level / Expert  
  - **EX**: Executive-level / Director  

- **employment_type**: The employment type for the role.
  - **PT**: Part-time  
  - **FT**: Full-time  
  - **CT**: Contract  
  - **FL**: Freelance  

- **job_title**: The role worked in during the year.

- **salary**: The total gross salary amount paid.

- **salary_currency**: The currency the salary was paid in (ISO 4217 code).

- **salary_in_usd**: Salary converted to USD (based on the dataset’s conversion method).

- **employee_residence**: The employee’s primary country of residence (ISO 3166 code).

- **remote_ratio**: The amount of work done remotely.
  - **0**: No remote work (less than 20%)  
  - **50**: Partially remote  
  - **100**: Fully remote (more than 80%)  

- **company_location**: The employer’s main office country (ISO 3166 code).

- **company_size**: Average number of employees at the company.
  - **S**: Less than 50 employees (small)  
  - **M**: 50 to 250 employees (medium)  
  - **L**: More than 250 employees (large)  
