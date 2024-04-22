import smtplib
import datetime as dt
import random
import pandas

my_email=" "
my_password=""

now=dt.datetime.now()
todays_day=now.day
todays_month=now.month

birthdays=pandas.read_csv("birthdays.csv")
birthdays_list=birthdays.to_dict("records")

for birthday in birthdays_list:
    if birthday["month"]==todays_month and birthday["day"]==todays_day:
        with open("letter.txt") as letter_file:
            letter=letter_file.readlines()
            name_line=letter[0].replace("[NAME]",birthday["name"])
            letter[0]=name_line

        letter_msg=""
        for line in letter:
            letter_msg+=line

        connection=smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email,password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday["email"],
                            msg=f"Subject:Birthday Wish\n\n{letter_msg}")
