#!/usr/bin/python

# SCRIPT TO AUTOMATE EMAILS

import smtplib
from dotenv import load_dotenv
import os
import time
import ssl
import sys
from read_glsheets import read_glsheets

start_time = time.perf_counter()

# load `.env` file
load_dotenv()

HOST: str = "smtp.gmail.com"
PORT: int = 465

login_email = os.getenv("login_email")
login_passwd = os.getenv("login_passwd")  # use `App Passwords` option in gmail (If 2 factor auth is enabled)

# reading google sheet data using link
link = sys.argv[1]
records = read_glsheets(link)

for index, record in enumerate(records, start=1):
	first_name = record.get("First Name")
	last_name = record.get("Last Name")
	receiver_email = record.get("Receiver")
	
	subject: str = "Automating Emails with Python Script - GOOGLE MAIL MERGE CLONE"
	body: str = f"Hai, {first_name} {last_name},\n\nI am Gowtham. I am a curious Python Programmer, Blogger. I write blogs on medium.com occasionally. Do check out my blogs here (medium.com/@gowtham180502).\n\nTo know more about me, then checkout gowtham.streamlit.app"

	# concatenate the `subject` and the `body` with `\n`
	msg = f"Subject: {subject}\n{body}"

	# add a layer of security to the email that we sent
	context = ssl.create_default_context()

	with smtplib.SMTP_SSL(HOST, PORT, context=context) as smtp:
		"""
		# This docsting code will be helpful, when the ssl is not used

		smtp.ehlo()  # this will call automatically in the background. But, even I explicitly calling here
		smtp.starttls()  # adding encryption to the n/w traffic
		smtp.ehlo()
		"""

		smtp.login(login_email, login_passwd)
	
		smtp.sendmail(login_email, receiver_email, msg)

	os.system("clear") if sys.platform == "linux" else os.system("cls")
	print(f"Progress: {index} of {len(records)} emails is sent")

end_time = time.perf_counter()

time_taken = end_time - start_time

print()
print(f"Script took {round(time_taken, 1)} second(s) to complete")
