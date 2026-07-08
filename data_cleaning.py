import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data.csv")

print("Original Data")
print(df)

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing Age with average age
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fill missing Salary with average salary
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

print("\nCleaned Data")
print(df)

# Save cleaned dataset
df.to_csv("cleaned_data.csv", index=False)

# Salary by Gender
salary = df.groupby("Gender")["Salary"].mean()

plt.figure(figsize=(6,4))
salary.plot(kind="bar")
plt.title("Average Salary by Gender")
plt.ylabel("Salary")
plt.savefig("images/bar_chart.png")
plt.close()

# Gender Distribution
gender = df["Gender"].value_counts()

plt.figure(figsize=(6,4))
gender.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Gender Distribution")
plt.savefig("images/pie_chart.png")
plt.close()

print("Project Completed Successfully")
