import argparse

def parse_arguments():
    description = """\
    This project is a clone of Mail Merge which is one of the extensions in google sheets using Python.
    """

    parser = argparse.ArgumentParser(description=description)

    # defining arguments for CLI
    parser.add_argument("link", help="expects google sheet public url")
    parser.add_argument("subject", help="expects subject for the email")
    parser.add_argument("content", help="expects text/HTML file path that contains message body")
    parser.add_argument("-cc", help="expects email addresses for Carbon Copy (CC)", nargs="+")
    parser.add_argument("-bcc", help="expects email addresses for Blind Carbon Copy (BCC)", nargs="+")
    parser.add_argument("-a", "--attach", help="expects file locations", nargs="+")

    args = parser.parse_args()

    return args
