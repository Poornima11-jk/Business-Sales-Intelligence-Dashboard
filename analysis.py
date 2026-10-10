import pandas as pd

df = pd.read_csv("sale_data.csv")

print("Sales Data:")
print(df)

print("\nTotal Sales:", df["Sales Amount"].sum())
print("Total Profit:", df["Profit"].sum())