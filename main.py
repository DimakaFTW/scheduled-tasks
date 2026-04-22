import random
import pandas
import datetime as dt
import smtplib
import os

# my_email = "dimo.sotirov93@gmail.com"
# password = "eugutmjzwbpjwfoi"
my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")

birthdays = pandas.read_csv("birthdays.csv")

today = dt.datetime.now()
day_month = (today.day, today.month)

birthdays_dict = {(data_row["day"], data_row["month"]): data_row for (index, data_row) in birthdays.iterrows()}

if day_month in birthdays_dict:

    with open(f"letter_templates/letter_{random.randint(1,3)}.txt", "r") as letter:
        str_letter = letter.read()
        personal_letter = str_letter.replace("[NAME]", birthdays_dict[day_month]["name"])

    with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthdays_dict[day_month]["email"],
                            msg=f"Subject:Happy Birthday\n\n{personal_letter}")





