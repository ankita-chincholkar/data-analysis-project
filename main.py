import pandas as pd

# Create sample data
data = {
    "Name": ["Ankita", "Riya", "Amit", "Rahul"],
    "Marks": [85, 90, 78, 88]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)

print("\nAverage Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())
