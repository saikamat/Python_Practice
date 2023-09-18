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

For further information, head to pytests/README.md

