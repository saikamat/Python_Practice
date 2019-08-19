# Python_Practice
Self study of python programming concepts.


## Keyboard Interrupt Handling mechanism
## File01:  	handling_keyboard_interrupts_f01.bash
## File02: record_some_stuff.py
this file  substitutes a recording process, which is rather long and continuous, and needs to be stopped by some external interrupt.
The interrupt is a keyboard interrupt of Shift+a or Shift+A combination.
The program runs the recording_ops() function. This operation is long and in certain cases continuous never ending loop. this needs to be interrupted by a keyboard interrupt.

So when recording_ops() is executing, if the user presses a Shift+a combination, the program will stop executing midway. The control will then pass to the ´handling_keyboard_interrupts_f01.bash´ file which called this script in the first place.

:)
