# Google-Mail-Merge-Clone
This project is a clone of `Mail Merge` which is one of the extensions in google sheets using `Python`

### .env file
The `.env` file is used to store environmental variables and it should definitely contain two things, one is login email address and password like below,
```bash
login_email="--YOUR EMAIL ADDRESS--"
login_passwd="--YOUR EMAIL PASSWORD--"
```

### How to Run
The `automate_emails.py` is the main python file which can be used to send emails. The following command will show you how run and how to provide google sheet url. Notably, the google sheet url should be publicly accessble. Open your terminal and type the following command,
```shell
python automate_emails.py "GOOGLE SHEET PUBLIC URL"
```
For more details, try help command on the file name
```shell
python automate_emails.py --help
```
#### Output
```shell
usage: automate_emails.py [-h] [-cc CC [CC ...]] [-bcc BCC [BCC ...]] link

This project is a clone of Mail Merge which is one of the extensions in google sheets using Python.

positional arguments:
  link                requires google sheet public url

options:
  -h, --help          show this help message and exit
  -cc CC [CC ...]     requires email addresses for Carbon Copy (CC)
  -bcc BCC [BCC ...]  requires email addresses for Blind Carbon Copy (BCC)
```
### References
* Article 1 - [2 easy ways to read Google Sheets data using Python](https://medium.com/geekculture/2-easy-ways-to-read-google-sheets-data-using-python-9e7ef366c775)
* Article 2 - [Google Sheet API Integration with Python](https://blog.devgenius.io/google-sheet-api-integration-with-python-1793795a9bc4)
* Video 1   - [How to send emails using Python](https://youtu.be/JRCJ6RtE3xU)
