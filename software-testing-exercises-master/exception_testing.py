import re
import pytest


def check_email_format(email):
    """check that the entered email format is correct"""
    if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        raise Exception("Invalid email format")
    else:
        return "Email format is ok"

@pytest.fixture()
def provide_email():
 yield "bademail.com"
 print("Cleanup after testing")


def test_email_exception(provide_email):
 """test that exception is raised for invalid emails"""
 print("testing email")
 with pytest.raises(Exception):
     assert check_email_format(provide_email)  # invalid email format to raise exception