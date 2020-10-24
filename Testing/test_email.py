import re
import pytest

import functions

def check_email_format(email):
    """check that the entered email format is correct"""
    if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        raise Exception("Invalid email format")
    else:
        return "Email format is ok"

    # def test_email_exception(a):
    #     """test that exception is raised for invalid emails"""
    #     with pytest.raises(Exception):
    #         assert check_email_format("bademail.com")  # invalid email format to raise exception

def provide_email():
    return 'bademail.com'


def test_email_exception():
    """test that exception is raised for invalid emails"""
    with pytest.raises(Exception):
        assert check_email_format(provide_email())  # invalid email format to raise exception



def test_ok():
    variable_ = 2 + 2
    variable4 = 4
    assert variable4 == variable_

def test_fun():
    str_variable = functions.prints()
    assert str_variable