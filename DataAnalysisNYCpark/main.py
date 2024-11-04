import pandas as pd
import csv

df = pd.read_csv("squirrel_data.csv")
column_name = "Primary Fur Color"
desired_column = df[column_name]
gray_count = df[df["Primary Fur Color"] == "Gray"].shape[0]
print(f"The color 'Gray' appears {gray_count} times.")

color_counts = df["Primary Fur Color"].value_counts()
print(color_counts)

color_counts_df = color_counts.reset_index()
color_counts_df.columns=["Fur Color", "Count"]

color_counts_df.to_csv("summarized_data.csv", index=False)
    