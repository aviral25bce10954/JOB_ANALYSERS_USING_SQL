import sqlite3
from prettytable import PrettyTable

conn = sqlite3.connect('job.db')
cursor = conn.cursor()

skills = [
    'Python', 'Java', 'C++', 'SQL', 'Machine Learning',
    'Data Science', 'Web Development', 'Android Development',
    'Cloud Computing', 'Cyber Security', 'AI',
    'Data Analysis', 'React', 'Node.js', 'DevOps',
    'Blockchain', 'UI/UX Design', 'Networking',
    'Software Testing', 'Django'
]

while True:
    print("\n----- JOB PORTAL -----")
    print("1. Apply for Job")
    print("2. Recruit Applicant")
    print("3. Check Trending Skills")
    print("4. Delete Application")
    print("5. Exit")

    try:
        ch = int(input("Enter choice: "))
    except:
        print("Please enter a valid number")
        continue

    if ch == 1:
        name = input("Enter your name: ")

        try:
            exp = int(input("Enter your experience (years): "))
            if exp < 0:
                print("Experience cannot be negative")
                continue
        except:
            print("Invalid experience")
            continue

        contact = input("Enter contact number: ")

        print("\nAvailable Skills:")
        for i, s in enumerate(skills, 1):
            print(i, s)

        print("\nEnter multiple skills (comma separated numbers, e.g. 1,3,5):")
        choices = input("Enter choices: ")

        selected_skills = []
        nums = choices.split(",")

        for num in nums:
            try:
                index = int(num.strip()) - 1
                if 0 <= index < len(skills):
                    selected_skills.append(skills[index])
            except:
                pass

        if not selected_skills:
            print("No valid skills selected")
            continue

        final_skills = ", ".join(selected_skills)

        cursor.execute(
            "INSERT INTO applicant (name, experience, skill, contact_number) VALUES (?, ?, ?, ?)",
            (name, exp, final_skills, contact)
        )
        conn.commit()

        print("Application submitted successfully")

    elif ch == 2:
        print("\nSelect required skill:")
        for i, s in enumerate(skills, 1):
            print(i, s)

        try:
            opt = int(input("Enter option number: "))
            if opt < 1 or opt > len(skills):
                print("Invalid choice")
                continue
            req_skill = skills[opt - 1]
        except:
            print("Invalid input")
            continue

        try:
            req_exp = int(input("Minimum experience needed: "))
        except:
            print("Invalid experience")
            continue

        
        cursor.execute(
            "UPDATE skills SET search_count = search_count + 1 WHERE skill_name = ?",
            (req_skill,)
        )
        conn.commit()

        cursor.execute(
            "SELECT name, experience, skill, contact_number FROM applicant WHERE skill LIKE ? AND experience >= ?",
            ('%' + req_skill + '%', req_exp)
        )

        data = cursor.fetchall()

        print("\nEligible Candidates:")

        table = PrettyTable()
        table.field_names = ["Name", "Experience", "Skill", "Contact"]

        if len(data) > 0:
            for d in data:
                table.add_row([d[0], d[1], req_skill, d[3]])
            print(table)
        else:
            print("No candidate found")

    elif ch == 3:
        cursor.execute(
            "SELECT skill_name, search_count FROM skills ORDER BY search_count DESC LIMIT 5"
        )

        top = cursor.fetchall()

        print("\nTop 5 In-Demand Skills:")

        table = PrettyTable()
        table.field_names = ["Skill", "Search Count"]

        for t in top:
            table.add_row([t[0], t[1]])

        print(table)

    elif ch == 4:
        name = input("Enter your name: ")
        contact = input("Enter your contact number: ")

        cursor.execute(
            "DELETE FROM applicant WHERE name = ? AND contact_number = ?",
            (name, contact)
        )
        conn.commit()

        if cursor.rowcount > 0:
            print("Application deleted successfully")
        else:
            print("No matching record found")

    elif ch == 5:
        print("Program closed")
        break

    else:
        print("Invalid choice")

conn.close()
