#! python
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# Seperate line and add stars
lines = text.split('\n')
for idx, line in enumerate(lines):
    lines[idx] = f"* {line}"
text = "\n".join(lines)
pyperclip.copy(text)
