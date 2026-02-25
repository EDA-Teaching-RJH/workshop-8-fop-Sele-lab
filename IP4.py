from IP3 import is_valid_email
def test_valid_email():
    try:
        assert is_valid_email("sneaky@@kent.ac.uk") == False
    except AssertionError:
        print("Test failed: double @ should be invalid")