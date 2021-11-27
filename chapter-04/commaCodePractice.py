def commafy(lst):
    if len(lst) == 0:
        return ""
    elif len(lst) == 1:
        return str(lst[0])
    elif len(lst) == 2:
        return str(lst[0]) + " and " + str(lst[1])
    else:
        lastItem = ", and " + str(lst.pop())
        return ", ".join([str(item) for item in lst]) + lastItem


empty = []
bacon = [42]
eggs = ["eggs", "spam"]
spam = ["apples", "bananas", "tofu", "cats"]
breakfast = ["ham", "spam", "spam", "spam", "eggs", "spam"]

print(commafy(empty))
print(commafy(bacon))
print(commafy(eggs))
print(commafy(spam))
print(commafy(breakfast))
