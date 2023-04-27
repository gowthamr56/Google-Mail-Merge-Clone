# Google-Mail-Merge-Clone
This project is a clone of `Mail Merge` which is one of the extensions in google sheets using `Python`
### How to Run
The `automate_emails.py` is the main python file which can be used to send emails. The following steps will show you how to run this project.
1. Clone this project.
```bash
git clone https://github.com/gowthamr56/Google-Mail-Merge-Clone.git
```
2. Install the required modules in the `requirements.txt`
```bash
pip install -r requirements.txt
```
3. Make sure you created `.env` file. The `.env` file is used to store environmental variables and it should definitely contain two things, one is login email address and password (use [App Passwords](https://myaccount.google.com/apppasswords) instead of using actual password) like below,
```bash
login_email="--YOUR EMAIL ADDRESS--"
login_passwd="--YOUR EMAIL PASSWORD--"
```
4. Then, create a google sheet and the google sheet must contain `Receiver` column which contains the receiver's email addresses. The google sheet url should be publicly available. For that, click <b>share -> General access ->  Anyone with a link</b>
5. Then, you need to create either HTML or TEXT file which contains the body of the email. Here, you can use placeholders (eg: {first_name}, {last_name}...) to generalize the emails according to the receiver. But, the google sheet must contain the columns with the same name that the placeholders has. The example text/html file should be like,
```html
<h3>Hello, Everyone</h3><p>I am a Gowtham. I am a curious Python Programmer, Blogger. I write blogs on <a href='medium.com/@gowtham180502'>medium</a> occasionally. To know more about me, then checkout <a href='gowtham.streamlit.app'>here</a></p>
``` 
6. The process is half done. Now, open your terminal/CMD and type the below command,
```shell
python automate_emails.py "GOOGLE SHEET URL" "EMAIL SUBJECT" "HTML/TEXT FILE PATH"
``` 
7. You can also specify some optional arguments. For an example,
* to specify BCC emails
```bash
python automate_emails.py "GOOGLE SHEET URL" "EMAIL SUBJECT" "HTML/TEXT FILE PATH" -bcc "person1@gmail.com" "person2@gmail.com" ...
```
* to specify CC emails
```bash
python automate_emails.py "GOOGLE SHEET URL" "EMAIL SUBJECT" "HTML/TEXT FILE PATH" -cc "person1@gmail.com" "person2@gmail.com" ...
```
* to attach files
```bash
python automate_emails.py "GOOGLE SHEET URL" "EMAIL SUBJECT" "HTML/TEXT FILE PATH" -a "file1" "file 2" ...  --OR--
python automate_emails.py "GOOGLE SHEET URL" "EMAIL SUBJECT" "HTML/TEXT FILE PATH" --attach "file1" "file 2" ...
```
For more details, try help command on the file name
```shell
python automate_emails.py --help
```
#### Output
```
usage: automate_emails.py [-h] [-cc CC [CC ...]] [-bcc BCC [BCC ...]] [-a ATTACH [ATTACH ...]] link subject content

This project is a clone of Mail Merge which is one of the extensions in google sheets using Python.

positional arguments:
  link                  expects google sheet public url
  subject               expects subject for the email
  content               expects text/HTML file path that contains message body

options:
  -h, --help            show this help message and exit
  -cc CC [CC ...]       expects email addresses for Carbon Copy (CC)
  -bcc BCC [BCC ...]    expects email addresses for Blind Carbon Copy (BCC)
  -a ATTACH [ATTACH ...], --attach ATTACH [ATTACH ...]
                        expects file locations
```
8. After the script is completely ran, all email has been sent and a log file has been created that contains the <b>timestamp</b> at which the email was sent.
### Time Complexity
Before implementing concurrency, script took <b>18 to 20 seconds</b> to send just four emails. But, after the implementation of concurrency, script took <b>9 to 10.5 seconds</b> to send the same four emails. And in the another case, the script took just <b>14.6 seconds</b> to send all the 20 emails.
### My References
* Article 1 - [2 easy ways to read Google Sheets data using Python](https://medium.com/geekculture/2-easy-ways-to-read-google-sheets-data-using-python-9e7ef366c775)
* Article 2 - [Google Sheet API Integration with Python](https://blog.devgenius.io/google-sheet-api-integration-with-python-1793795a9bc4)
* Video 1   - [How to send emails using Python](https://youtu.be/JRCJ6RtE3xU)
