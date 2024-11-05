import smtplib
import datetime as dt
import pandas as pd
import os
import random

# Enter email & app password to send the email
MY_EMAIL = ""
PASSWORD = ""

# Read the birthdays.csv file
df = pd.read_csv("birthdays.csv")

# Get today's date
today = dt.datetime.today()
today_day = today.day
today_month = today.month

# Folder containing letter templates
folder_path = "letter_templates"
files = os.listdir(folder_path)

# Iterate through the DataFrame rows
for index, row in df.iterrows():
    # Check if today matches the birthday
    if today_day == row["day"] and today_month == row["month"]:
        # Pick a random letter template
        random_file = random.choice(files)
        with open(os.path.join(folder_path, random_file), "r") as file:
            content = file.read()
            personalized_letter = content.replace("[NAME]", row["name"])

            # Send the email
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(MY_EMAIL, PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=row["email"],
                    msg=f"Subject:Happy Birthday\n\n{personalized_letter}"
                )




