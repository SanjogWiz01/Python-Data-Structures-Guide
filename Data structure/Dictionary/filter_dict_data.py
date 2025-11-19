# dict_filtering.py

# Filtering dictionary values
data = {"sanjog": 90, "aakriti": 75, "sandhya": 88, "er sayeb": 60}

# Keep only high scorers (>80)
high_scores = {k: v for k, v in data.items() if v > 80}
print("High Scores:", high_scores)

# Filter keys based on a list
selected_keys = ["sanjog", "aakriti"]
filtered_dict = {k: data[k] for k in selected_keys}
print("Filtered Dict by Keys:", filtered_dict)
print("Original Dict:", data)
