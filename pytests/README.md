### 1.1 Other good commands
```
pytest -v ## verbose

pytest -v -s ## also print logs
```

#### 1.1.1 Sample assertion error log
```
pytest -v -s
```
Test Case Log:-
```
─    ~/Lo/p/i/Sama/Python_Practice/pytests    master !2 ──────── ✔  script_env   18:20:37  ─╮
╰─ pytest -v -s                                                                                         ─╯
=========================================== test session starts ===========================================
platform darwin -- Python 3.9.6, pytest-7.4.2, pluggy-1.3.0 -- /Users/saikamat/Local Documents/scripts/script_env/bin/python3
cachedir: .pytest_cache
rootdir: /Users/saikamat/Local Documents/personal_docs/interviews/Sama/Python_Practice/pytests
collected 2 items                                                                                         

test_demo1.py::test_firstProgram hello world
PASSED
test_demo2.py::test_secondProgram FAILED

================================================ FAILURES =================================================
___________________________________________ test_secondProgram ____________________________________________

    def test_secondProgram():
        input_message = "Hello"
>       assert input_message == "Helo", "Test failed because the messaged don't match."
E       AssertionError: Test failed because the messaged don't match.
E       assert 'Hello' == 'Helo'
E         - Helo
E         + Hello
E         ?    +

test_demo2.py:6: AssertionError
========================================= short test summary info =========================================
FAILED test_demo2.py::test_secondProgram - AssertionError: Test failed because the messaged don't match.
======================================= 1 failed, 1 passed in 0.15s =======================================
```


> In `pytest` different pieces of code should have different test method names. I.e. each method name must be **unique**

----
### 1.2 Pytest on specific files and specific commands

#### 1.2.1 To run `pytest` on specific files only
```
pytest <<filename>>.py 
```

Sample Log
```
╭─    ~/Lo/p/i/Sama/Python_Practice/pytests    master !2 ?2 ────── 1 ✘  script_env   19:34:55  ─╮
╰─ pytest test_specific_tests_only.py -v -s                                                                ─╯
============================================ test session starts =============================================
platform darwin -- Python 3.9.6, pytest-7.4.2, pluggy-1.3.0 -- /Users/saikamat/Local Documents/scripts/script_env/bin/python3
cachedir: .pytest_cache
rootdir: /Users/saikamat/Local Documents/personal_docs/interviews/Sama/Python_Practice/pytests
collected 2 items                                                                                            

test_specific_tests_only.py::test_SquarePolygons PASSED
test_specific_tests_only.py::test_SignCheck FAILED

================================================== FAILURES ==================================================
_______________________________________________ test_SignCheck _______________________________________________

    def test_SignCheck():
        sign_read = "STOP"
>       assert sign_read == "HALT", "Sign is not the Stop sign"
E       AssertionError: Sign is not the Stop sign
E       assert 'STOP' == 'HALT'
E         - HALT
E         + STOP

test_specific_tests_only.py:26: AssertionError
========================================== short test summary info ===========================================
FAILED test_specific_tests_only.py::test_SignCheck - AssertionError: Sign is not the Stop sign
======================================== 1 failed, 1 passed in 0.06s =========================================
```

#### 1.2.2 To run `pytest` on specific files and specific commands
```
pytest <<filename>>.py -k "<<keyword>>"
```

Sample Log
```

╭─    ~/Lo/p/i/Sama/Python_Practice/pytests    master !2 ?2 ────── 1 ✘  script_env   19:35:26  ─╮
╰─ pytest test_specific_tests_only.py -v -s -k "Polygon"                                                   ─╯
============================================ test session starts =============================================
platform darwin -- Python 3.9.6, pytest-7.4.2, pluggy-1.3.0 -- /Users/saikamat/Local Documents/scripts/script_env/bin/python3
cachedir: .pytest_cache
rootdir: /Users/saikamat/Local Documents/personal_docs/interviews/Sama/Python_Practice/pytests
collected 2 items / 1 deselected / 1 selected                                                                

test_specific_tests_only.py::test_SquarePolygons PASSED

====================================== 1 passed, 1 deselected in 0.00s =======================================
```

----
### 1.3 To `pyrtest` only specific commands based on certain conditions

#### 1.3.1 Skip a test function entirely
Input command `@pytest.mark.skip` above the test function that is to be skipped in the tests
```
@pytest.mark.skip
def foo():
    # do something
```

Sample Output log
```
╭─    ~/Lo/p/i/Sama/Python_Practice/pytests    master !1 ───────── 1 ✘  script_env   20:03:06  ─╮
╰─ pytest test_specific_tests_only.py -v -s                                                                ─╯
============================================ test session starts =============================================
platform darwin -- Python 3.9.6, pytest-7.4.2, pluggy-1.3.0 -- /Users/saikamat/Local Documents/scripts/script_env/bin/python3
cachedir: .pytest_cache
rootdir: /Users/saikamat/Local Documents/personal_docs/interviews/Sama/Python_Practice/pytests
collected 2 items                                                                                            

test_specific_tests_only.py::test_SquarePolygons FAILED
test_specific_tests_only.py::test_SignCheck SKIPPED (unconditional skip)

================================================== FAILURES ==================================================
____________________________________________ test_SquarePolygons _____________________________________________

    def test_SquarePolygons():
        ax = 0
        ay = 0
        bx = 0
```


#### 1.3.2 Test a test function but ignore the results
Sometimes, the variables inside a test function are crucial to other tests. However it may be possible that that function might be completely buggy. In such scenarios, though the test function will fail, we need the variables. Here a mere `skip` will **not help***.

Therefore use `@pytest.mark.xfail`

```
@pytest.mark.xfail
def foo():
    # do something
```

Sample output log
```
─    ~/Lo/p/interviews/Sama/Python_Practice/pytests    master !2 ── ✔  script_env   20:08:59  ─╮
╰─ pytest test_specific_tests_only.py -v -s                                                                ─╯
============================================ test session starts =============================================
platform darwin -- Python 3.9.6, pytest-7.4.2, pluggy-1.3.0 -- /Users/saikamat/Local Documents/scripts/script_env/bin/python3
cachedir: .pytest_cache
rootdir: /Users/saikamat/Local Documents/personal_docs/interviews/Sama/Python_Practice/pytests
collected 2 items                                                                                            

test_specific_tests_only.py::test_SquarePolygons XFAIL
test_specific_tests_only.py::test_SignCheck SKIPPED (unconditional skip)

======================================= 1 skipped, 1 xfailed in 0.02s ========================================
```

---
### 1.4 Ordered Sequential Testing

Use the `@pytest.fixture()` command

So in the below code, the `intial_function()` will be executed before the `test_initial_function()`
```
@pytest.fixture()
def initial_function():
    # do something

def test_initial_function()
    # do something
```

Executing the command
```
pytest <<filename>>.py -s
```

Output Log
```

╭─    ~/Lo/p/i/Sama/Python_Practice/pytests    master !1 ?1 ──────── ✔  script_env   21:30:07  ─╮
╰─ pytest test_ordered_sequential_tests_demo.py -s                                                         ─╯
============================================ test session starts =============================================
platform darwin -- Python 3.9.6, pytest-7.4.2, pluggy-1.3.0
rootdir: /Users/saikamat/Local Documents/personal_docs/interviews/Sama/Python_Practice/pytests
collected 1 item                                                                                             

test_ordered_sequential_tests_demo.py Setup - Opening Web Browser / Console...
Test Result -> Browser Opened.
.Setup - Closing Browser...
Setup - Browser closed.


============================================= 1 passed in 0.00s ==============================================
```

---
