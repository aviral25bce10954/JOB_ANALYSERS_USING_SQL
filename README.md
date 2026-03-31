# Job Portal Analyzer

A menu-driven job portal system built using Python and SQLite. It allows applicants to register with multiple skills and enables recruiters to efficiently search and filter candidates based on requirements. The system also keeps track of skill demand trends based on recruiter activity.

---

## Features

* Apply for job with multiple skills
* Recruit applicants using skill and experience filters
* Displays only matched skill in results
* Delete application using name and contact
* Tracks skill demand based on recruiter searches
* Shows top 5 most in-demand skills
* Input validation to prevent errors
* Tabular output using PrettyTable

---

## Technologies Used

| Technology  | Purpose                |
| ----------- | ---------------------- |
| Python      | Core application logic |
| SQLite      | Database management    |
| PrettyTable | Clean tabular output   |

---

## Database Structure

### Applicant Table

| Field Name     | Description                       |
| -------------- | --------------------------------- |
| id             | Unique ID                         |
| name           | Applicant name                    |
| experience     | Years of experience               |
| skill          | Multiple skills (comma-separated) |
| contact_number | Contact details                   |

---

### Skills Table

| Field Name   | Description                               |
| ------------ | ----------------------------------------- |
| skill_name   | Skill name                                |
| search_count | Tracks how frequently a skill is searched |

---

## How to Run

```bash id="f7q2hz"
pip install prettytable
python job_analyser.py
```

---

## Key Functionalities

### Apply for Job

Applicants can enter their details and select multiple skills. The system stores structured data which helps in understanding applicant profiles.

### Recruit Applicant

Recruiters can filter candidates based on required skills and experience. The system uses condition-based selection to display relevant candidates.

### Trend Analyzer

The system records how often each skill is searched and displays the top 5 most in-demand skills. This helps in identifying patterns in job market demand.

### Delete Application

Applicants can remove their data securely using their name and contact number.

---

## Future Improvements

* Graphical User Interface (GUI)
* Login system
* Resume upload
* Intelligent recommendation system for jobs and candidates
* Predictive insights for skill demand

---

## Conclusion

This project demonstrates how Python and SQLite can be used to build a functional job portal system. It also provides insights into handling structured data, filtering logic, and identifying patterns in user activity, making it useful for understanding real-world job market behavior.
