import pandas as pd

data = {
    "Name": ["Aman", "Mehul", "Alok"],
    "Age": [20, 21, 22],
    "City": ["Ahmedabad", "Surat", "Vadodara"]
}
df = pd.DataFrame(data)
print("Orignal Dataset:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDataset after Handling Missing Values:")
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["City"] = df["City"].fillna(df["City"].mode()[0])
print(df)

df = df.drop_duplicates()
df = df.reset_index(drop=True)

print("\nPreprocessed Dataset:")
print(df)
