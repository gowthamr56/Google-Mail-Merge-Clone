#!/usr/bin/python

# SCRIPT TO AUTOMATE EMAILS

import smtplib
from dotenv import load_dotenv
import os
import time
import ssl
import sys
from read_glsheets import read_glsheets
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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

	msg = MIMEMultipart("alternative")

	msg["Subject"] = "Automating Emails with Python Script - GOOGLE MAIL MERGE CLONE"
	
	html_body = f"""\
	<html>
	<body>
		<h2>Hai {first_name} {last_name}</h2>
		<p>I am a Gowtham. I am a curious Python Programmer, Blogger. I write blogs on <a href='medium.com/@gowtham180502'>medium</a> occasionally</p>
		<p>To know more about me, then checkout <a href='gowtham.streamlit.app'>here</a>.</p>
	</body>
	</html>
	"""
	content = MIMEText(html_body, "html")

	msg.attach(content)

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
	
		smtp.sendmail(login_email, receiver_email, msg.as_string())

	os.system("clear") if sys.platform == "linux" else os.system("cls")
	print(f"Progress: {index} of {len(records)} emails is sent")

end_time = time.perf_counter()

time_taken = end_time - start_time

print()
print(f"Script took {round(time_taken, 1)} second(s) to complete")
