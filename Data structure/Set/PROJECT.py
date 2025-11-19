# employee_skills_analysis.py

import random

# Sample data: employees and their skills
employees = {
    "Alice": {"Python", "SQL", "Machine Learning"},
    "Bob": {"Python", "R", "SQL"},
    "Charlie": {"Python", "SQL", "Deep Learning"},
    "David": {"Python", "SQL", "Machine Learning", "R"},
    "Eva": {"SQL", "Python", "Deep Learning"}
}

departments = {
    "IT": {"Alice", "Bob"},
    "AI": {"Charlie", "David"},
    "Data": {"Eva", "Alice"}
}

# 1️⃣ All unique skills in the company
all_skills = set().union(*employees.values())
print("All Unique Skills:", all_skills)

# 2️⃣ Skills every employee has
common_skills = set.intersection(*employees.values())
print("Skills everyone has:", common_skills)

# 3️⃣ Unique skills per employee
unique_skills = {name: skills - common_skills for name, skills in employees.items()}
print("Unique Skills per Employee:", unique_skills)

# 4️⃣ Rare skills in the company (appear only once)
skill_count = {}
for skills in employees.values():
    for skill in skills:
        skill_count[skill] = skill_count.get(skill, 0) + 1

rare_skills = {skill for skill, count in skill_count.items() if count == 1}
print("Rare Skills in Company:", rare_skills)

# 5️⃣ Department-wise skill analysis
dept_skills = {}
for dept, emp_list in departments.items():
    dept_skills[dept] = set().union(*(employees[e] for e in emp_list))
print("Department-wise Skills:", dept_skills)

# 6️⃣ Employees with subset of a skill set (e.g., Machine Learning group)
ml_group = {e for e, s in employees.items() if "Machine Learning" in s}
print("Employees skilled in Machine Learning:", ml_group)

# 7️⃣ Random skill sampling for training session
sampled_skills = random.sample(all_skills, 3)
print("Random Skills for Training:", sampled_skills)

# 8️⃣ Skills overlap between two departments
dept_overlap = dept_skills["IT"] & dept_skills["AI"]
print("Skills common between IT and AI:", dept_overlap)
# 9️⃣ Employees with no unique skills
no_unique_skills = {name for name, skills in unique_skills.items() if not skills}
print("Employees with no unique skills:", no_unique_skills)