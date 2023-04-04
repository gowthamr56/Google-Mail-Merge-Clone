#!/usr/bin/python

# SCRIPT TO AUTOMATE EMAILS

from dotenv import load_dotenv
import os
import time
import sys
from read_glsheets import read_glsheets
import yagmail
import argparse

start_time = time.perf_counter()

# load `.env` file
load_dotenv()

description = """\
This project is a clone of Mail Merge which is one of the extensions in google sheets using Python.
"""

parser = argparse.ArgumentParser(description=description)

# defining arguments for CLI
parser.add_argument("link", help="requires google sheet public url")
parser.add_argument("-cc", help="requires email addresses for Carbon Copy (CC)", nargs="+")
parser.add_argument("-bcc", help="requires email addresses for Blind Carbon Copy (BCC)", nargs="+")

args = parser.parse_args()

HOST: str = "smtp.gmail.com"
PORT: int = 465

login_email = os.getenv("login_email")
login_passwd = os.getenv("login_passwd")  # use `App Passwords` option in gmail (If 2 factor auth is enabled)

cc = args.cc
bcc = args.bcc

subject = "GOOGLE MAIL MERGE CLONE"

# reading google sheet data using link
link = sys.argv[1]
records = read_glsheets(link)

# initialization
smtp = yagmail.SMTP(user=login_email, password=login_passwd, host=HOST, port=PORT)

for index, record in enumerate(records, start=1):
	first_name = record.get("First Name")
	last_name = record.get("Last Name")
	receiver_email = record.get("Receiver")

	message_body = f"""\
	<html>
	<body>
		<h3>Hai {first_name} {last_name}</h3>
		<p>I am a Gowtham. I am a curious Python Programmer, Blogger. I write blogs on <a href='medium.com/@gowtham180502'>medium</a> occasionally</p>
		<p>To know more about me, then checkout <a href='gowtham.streamlit.app'>here</a>.</p>
	</body>
	</html>
	"""

	smtp.send(to=receiver_email, cc=cc, bcc=bcc, subject=subject, contents=message_body)

	os.system("clear") if sys.platform == "linux" else os.system("cls")
	print(f"Progress: {index} of {len(records)} emails is sent")

# to close the SMTP server connection 
smtp.close()

end_time = time.perf_counter()

time_taken = end_time - start_time

print()
print(f"Script took {round(time_taken, 1)} second(s) to complete")
