import argparse

def parse_arguments():
    description = """\
    This project is a clone of Mail Merge which is one of the extensions in google sheets using Python.
    """

    parser = argparse.ArgumentParser(description=description)

    # defining arguments for CLI
    parser.add_argument("link", help="requires google sheet public url")
    parser.add_argument("-cc", help="requires email addresses for Carbon Copy (CC)", nargs="+")
    parser.add_argument("-bcc", help="requires email addresses for Blind Carbon Copy (BCC)", nargs="+")

    args = parser.parse_args()

    return args
