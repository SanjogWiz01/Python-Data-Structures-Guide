# merge_dicts_for_features.py

# Feature engineering: combining multiple dictionaries
age = {"Alice": 25, "Bob": 30, "Charlie": 28}
salary = {"Alice": 50000, "Bob": 60000, "Charlie": 55000}
department = {"Alice": "HR", "Bob": "IT", "Charlie": "Finance"}

# Merge dicts into a single dict of dicts
from collections import defaultdict

combined = defaultdict(dict)
for key, value in age.items():
    combined[key]["Age"] = value
for key, value in salary.items():
    combined[key]["Salary"] = value
for key, value in department.items():
    combined[key]["Department"] = value

print("Combined Dict:\n", dict(combined))
