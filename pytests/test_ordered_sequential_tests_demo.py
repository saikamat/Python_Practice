import pytest

## the `fixture()` tag mandates that function underneath it be executed first.
## It's necessary that the test function should be connected to the initial function.
@pytest.fixture()
def setup():
    print("Setup - Opening Web Browser / Console...")

    # now that initial setup is tested, make the test continue with the setup 
    # with the `yield` command
    yield
    print("Setup - Closing Browser...")
    print("Setup - Browser closed.")

def test_opening_browser(setup):
    print("Test Result -> Browser Opened.")