# dictionary_in_pandas_style.py
data = {
    "Name": ["Sanjog", "Nisha", "Aarav"],
    "Age": [18, 19, 20],
    "Marks": [90, 85, 95]
}

for i in range(len(data["Name"])):
    print(f"{data['Name'][i]} | Age: {data['Age'][i]} | Marks: {data['Marks'][i]}")
