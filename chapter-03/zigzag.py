import time
import sys

indent = 0
indentIncreasing = True

try:
    while True:  # Main programming loop
        print(" " * indent, end="")
        print("*" * 7)
        time.sleep(0.05)

        if indentIncreasing:
            indent += 1
            if indent == 20:
                indentIncreasing = False
        else:
            indent -= 1
            if indent == 0:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
