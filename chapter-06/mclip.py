#!/usr/bin/env python
# mclip.py - A multi-clipboard program.

import sys
import pyperclip


TEXT = {
    "agree": """Yes, I agree. That sounds fine to me.""",
    "busy": """Sorry, can we do this later this week or next week?""",
    "upsell": """Would you consider making this a monthly donation?""",
}


if len(sys.argv) < 2:
    print("Usage: python mclip.py [keyphrase] - copy phrase text")
    sys.exit()

keyphrase = sys.argv[1]  # first command line arg is the key phrase

while True:
    if keyphrase in TEXT:
        pyperclip.copy(TEXT[keyphrase])
        print(f"Text for {keyphrase} copied to clipboard.")
        break
    else:
        choices = [word for word in TEXT.keys()]
        print(f"There is no text for '{keyphrase}'")
        print(f"Available commands are:")
        for word in choices:
            print(word.rjust(8))
        keyphrase = input("Which phrases would you like to use? ")
