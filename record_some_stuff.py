from pynput import keyboard

# The key combination to check
COMBINATIONS = [
    {keyboard.Key.shift, keyboard.KeyCode(char='a')},
    {keyboard.Key.shift, keyboard.KeyCode(char='A')}
]

# The currently active modifiers
current = set()

print('Recording Script executing...')
print('Press Shift+a to stop recording.')

# this function substitutes a recording process, which is rather long and continuous, and needs to be stopped by some external interrupt.
def recording_op():
    print('just stalling...')
    for i in range(10000):
        for j in range(1000):
            pass


recording_op()


def execute():
    print("Stopping recording...")
    exit()


def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()


def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
