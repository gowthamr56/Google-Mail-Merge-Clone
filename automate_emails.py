#!/usr/bin/python

# SCRIPT TO AUTOMATE EMAILS

from dotenv import load_dotenv
import os
import time
import sys
import yagmail
from read_glsheets import read_glsheets
from argument_parser import parse_arguments

start_time = time.perf_counter()

# load `.env` file
load_dotenv()

HOST: str = "smtp.gmail.com"
PORT: int = 465

login_email = os.getenv("login_email")
login_passwd = os.getenv("login_passwd")  # use `App Passwords` option in gmail (If 2 factor auth is enabled)

parse_args = parse_arguments()

# parsed arguments
link = parse_args.link
subject = parse_args.subject
content_file = parse_args.content
cc = parse_args.cc
bcc = parse_args.bcc
attachments = parse_args.attach

# reading google sheet data using link
records = read_glsheets(link)

# reading content file
with open(content_file, "r") as file:
	msg_body = file.read()

# yagmail initialization
smtp = yagmail.SMTP(user=login_email, password=login_passwd, host=HOST, port=PORT)

for index, record in enumerate(records, start=1):
	to = record.get("Receiver")
	content = msg_body.format(**record)

	smtp.send(to=to, cc=cc, bcc=bcc, subject=subject, contents=content, attachments=attachments)

	os.system("clear") if sys.platform == "linux" else os.system("cls")
	print(f"Progress: {index} of {len(records)} emails is sent")

# to close the SMTP server connection 
smtp.close()

end_time = time.perf_counter()
time_taken = end_time - start_time
print()
print(f"Script took {round(time_taken, 1)} second(s) to complete")
