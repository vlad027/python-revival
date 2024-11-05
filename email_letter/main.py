import smtplib
import datetime as dt
import pandas as pd
import os
import random

#Enter email & app password to send the email
MY_EMAIL = ""
PASSWORD = ""

df = pd.read_csv("birthdays.csv")

today = dt.datetime.today().weekday()

folder_path = "letter_templates"
files = os.listdir(folder_path)
random_file = random.choice(files)

for index, row in df.iterrows():
    if today == row["weekday"]:
        with open(os.path.join(folder_path, random_file), "r") as file:
            content = file.read()
            personalized_letter = content.replace("[NAME]", row["name"])

            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(MY_EMAIL, PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=row["email"],
                    msg=f"Subject:Happy Birthday\n\n{personalized_letter}")




