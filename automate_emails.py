#!/usr/bin/python

# SCRIPT TO AUTOMATE EMAILS

from dotenv import load_dotenv
import os
import time, datetime
import sys
import yagmail
import csv
from typing import Optional
import threading
from read_glsheets import read_glsheets
from argument_parser import parse_arguments

start_time = time.perf_counter()

os.system("clear") if sys.platform == "linux" or "darwin" else os.system("cls")

def send_emails(login_email: str, login_passwd: str, host: int, port: int, records: list, subject: str, log_writer, cc: Optional[list] = None, bcc: Optional[list] = None, attachments: Optional[str] = None) -> None:
	# yagmail initialization
	smtp = yagmail.SMTP(user=login_email, password=login_passwd, host=host, port=port)

	for record in records:
		to = record.get("Receiver")
		content = msg_body.format(**record)

		smtp.send(to=to, cc=cc, bcc=bcc, subject=subject, contents=content, attachments=attachments)

		log_writer.writerow([to, datetime.datetime.now().strftime("%d-%m-%y, %H:%M:%S")])

		print(f"Mail sent to {to}")


	# to close the SMTP server connection 
	smtp.close()

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

# spliting the records into chuncks (each chuncks having 2 records)
CHUNCK_SIZE: int = 2
record_chuncks = [records[index:(index + CHUNCK_SIZE)] for index in range(0, len(records), CHUNCK_SIZE)]
rchuncks_len = len(record_chuncks)

# reading content file
with open(content_file, "r") as file:
	msg_body = file.read()


# logging
log_fname = "log.csv"

if not log_fname in os.listdir():
	log_file = open(log_fname, "w")

	log_writer = csv.writer(log_file)
	log_writer.writerow(["Receiver", "Received At"])
else:
	log_file = open(log_fname, "a")

	log_writer = csv.writer(log_file)
	if os.path.getsize(log_fname) == 0:
		log_writer.writerow(["Receiver", "Received At"])

# creating threads, each thread will handle 2 mails.
threads = [threading.Thread(target=send_emails, args=(login_email, login_passwd, HOST, PORT, record_chunck, subject, log_writer, cc, bcc, attachments)) for record_chunck in record_chuncks]

# starting all the threads
for thread in threads:
	thread.start()


for thread in threads:
	thread.join()

log_file.close()

end_time = time.perf_counter()
time_taken = end_time - start_time
print()
print(f"Script took {round(time_taken, 1)} second(s) to complete")
