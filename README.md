 JOB_ANALYSERS_USING_SQL
Menu-driven Python + SQLite job portal. Applicants can register with multiple skills, experience and contact. Recruiters filter candidates by skill and experience. System tracks search trends and shows top in-demand skills. Includes delete option, validation and PrettyTable-based output.
 Job Portal Analyzer (Python + SQLite)

 📌 Overview

This project is a menu-driven job portal system built using Python and SQLite. It allows applicants to apply for jobs and recruiters to search for suitable candidates based on skills and experience. The system also tracks trending skills based on recruiter searches.

---

 🚀 Features

* Apply for job with multiple skills
* Recruit applicants based on skill and experience
* Display only matched skill in results
* Delete application using name and contact
* Track and display top 5 in-demand skills
* Clean tabular output using PrettyTable
* Input validation to avoid runtime errors

---

 🛠️ Technologies Used

* Python
* SQLite3
* PrettyTable

---

 📂 Database Structure

 1. Applicant Table

* id (Primary Key)
* name
* experience
* skill (comma-separated for multiple skills)
* contact_number

 2. Skills Table

* skill_name (Primary Key)
* search_count

---

 ▶️ How to Run

1. Install required library:

   ```
   pip install prettytable
   ```
2. Run the program:

   ```
   python job_analyser.py
   ```
3. Follow the menu options in terminal

---

 📊 Functionality

 Apply for Job

User enters name, experience, contact and selects multiple skills.

 Recruit Applicant

Recruiter selects skill and required experience. Matching candidates are displayed.

 Trend Analyzer

Shows top 5 most searched skills based on recruiter activity.

 Delete Application

Applicant can remove their record using name and contact number.

---

 💡 Key Concepts Used

* Menu-driven programming
* SQL queries (INSERT, SELECT, UPDATE, DELETE)
* Data filtering using LIKE
* List handling and string manipulation

---

 📈 Future Improvements

* GUI using Tkinter
* Login system (Applicant/Recruiter)
* Resume upload and ranking system
* Advanced recommendation system

---

 👨‍💻 Author

Developed as a mini project for academic purposes.
