import re


def regexStrip(string, char=" "):
    if char in ".^$*+?{}[]\\|()":
        char = f"\\{char}"
    ending = re.compile(f"^{char}*(.*)").search(string)
    if ending:
        ending = ending.groups()[0]
    else:
        ending = string
    answer = re.compile(f"(.*?){char}*$").search(ending)
    if answer:
        answer = answer.groups()[0]
    else:
        answer = ending
    return answer


# Tests
print(regexStrip("    Testing Testing    "))
print(regexStrip("...123...456...", "."))
print(regexStrip("...123 456", "."))
print(regexStrip("  123 456  ...", "."))
print(regexStrip("\\/\\/\\/\\/\\/"))
print(regexStrip("\\/\\/\\/\\/\\/", "/"))
