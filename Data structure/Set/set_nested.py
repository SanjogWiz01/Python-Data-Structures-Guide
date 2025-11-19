# Example of a nested set structure
nested = [
    {"Python", "SQL"},
    {"SQL", "R"},
    {"Python", "Deep Learning"}
]

# All unique skills
all_skills = set().union(*nested)
print("All Unique Skills:", all_skills)
