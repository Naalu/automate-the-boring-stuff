import re


def isPasswordStrong(password):
    hasDigit = re.compile(r"\d").search(password)
    hasLower = re.compile(r"[a-z]").search(password)
    hasUpper = re.compile(r"[A-Z]").search(password)
    atLeastEight = re.compile(r"\S{8,}").search(password)

    return bool(hasDigit and hasLower and hasUpper and atLeastEight)


for test in ["A12345678a", "Aa1", "AB12345678", "ab12345678", "AaBbCcDd", "123abcABC"]:
    print(f"{test}: {isPasswordStrong(test)}")
