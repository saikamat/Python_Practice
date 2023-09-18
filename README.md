# Python_Practice
Self study of python programming concepts.


## 1. Keyboard Interrupt Handling mechanism
### 1.1 Pre-requisites
Install `pynput` package using `pip install pynput`

#### 1.1.1 File01: handling_keyboard_interrupts_f01.bash
#### 1.1.2 File02: record_some_stuff.py
this file  substitutes a recording process, which is rather long and continuous, and needs to be stopped by some external interrupt.
The interrupt is a keyboard interrupt of `Shift`+`a` or `Shift`+`A` combination.
The program runs the `recording_ops()` function. This operation is long and in certain cases continuous never ending loop. this needs to be interrupted by a keyboard interrupt.

So when `recording_ops()` is executing, if the user presses a `Shift`+`a` combination, the program will stop executing midway. The control will then pass to the `handling_keyboard_interrupts_f01.bash` file which called this script in the first place.

:)

## 2. Running pytest
### 2.1 Install pytest
```
pip install pytest
```

#### 2.1.1 Create test module
- Always create test files with either suffix or prefix as `test_`
- All code should be inside test functions

#### 2.1.2 Running the module
```
pytest <<test_file_name>>.py
```

### 2.2 Other good commands
```
pytest -v ## verbose

pytest -v -s ## also print logs
```

#### 2.2.1 Sample assertion error log
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


### 2.3 Pytest on specific files and specific commands

#### 2.3.1 To run `pytest` on specific files only
```
pytest <<filename>>.py 
```

#### Sample Log
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

#### 2.3.2 To run `pytest` on specific files and specific commands
```
pytest <<filename>>.py -k "<<keyword>>"
```

#### Sample Log
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