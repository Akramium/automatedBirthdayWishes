import datetime as dt
import random
import smtplib

import pandas

MY_EMAIL = ""
MY_PASSWORD = ""

today = dt.datetime.now()
birthdays = pandas.read_csv("birthdays.csv")

birthday = birthdays[(birthdays['day'] == today.day) & (birthdays["month"] == today.month)]
if not birthday.empty:
    letter_num = random.randint(1, 3)
    with open(f"letter_templates/letter_{letter_num}.txt") as letter:
        letter = letter.read()
        new_letter = letter.replace("[NAME]", birthday["name"].to_string(index=False))
        with smtplib.SMTP(host="smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday["email"].to_string(index=False),
                msg=f"Subject:Happy Birthday!\n\n{new_letter}"
            )
