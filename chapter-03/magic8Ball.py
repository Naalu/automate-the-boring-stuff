import random


def getAnswer(answerNumber):
    return {
        1: "It is certain",
        2: "It is decidedly so",
        3: "Yes",
        4: "Reply hazy try again",
        5: "Ask again later",
        6: "Concentrate and ask again",
        7: "My reply is no",
        8: "Outlook not so good",
        9: "Very doubtful",
    }.get(answerNumber)


r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
