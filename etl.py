import pandas as pd

df = pd.read_csv('raw_data.csv')

df['name'] = df['name'].str.capitalize()

df = df.dropna(subset=['age'])

df['age'] = df['age'].astype(int)

df.to_csv('cleaned_data.csv', index=False)

print("✅ Cleaned data saved to cleaned_data.csv!")