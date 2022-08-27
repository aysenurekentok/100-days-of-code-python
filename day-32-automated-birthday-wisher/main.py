import random
import datetime as dt
import smtplib
import pandas

# Enter YOUR email and password
email = ""
email_password = ""

now = dt.datetime.now()
birthday = (now.day, now.month)

data = pandas.read_csv("birthdays.csv")
people = {(row.day, row.month): row["name"] for (index, row) in data.iterrows()}

if birthday in people:
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as file:
        text = file.read()
        name = people[birthday]
        letter = text.replace("[NAME]", name)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=email_password)
        connection.sendmail(
            from_addr=email,
            to_addrs=data["email"],
            msg=f"Subject:Birthday wishes!\n\n{letter}"
        )
