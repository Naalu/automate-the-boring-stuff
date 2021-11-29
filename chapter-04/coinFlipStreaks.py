import random

numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creats a list of 100 'heads' or 'tails' values.
    flips = ["heads" if random.randint(0, 1) == 1 else "tails" for flip in range(100)]
    # Code that checks if there is a streak of 6 heads or tails values in a row.
    sequenceLengths = []
    currentStreakType = flips[0]
    currentStreakLength = 0
    for idx, flip in enumerate(flips):
        currentFlip = flips[idx]
        if currentFlip == currentStreakType:
            currentStreakLength += 1
        else:
            sequenceLengths.append(currentStreakLength)
            currentStreakLength = 1
            currentStreakType = currentFlip
    numberOfStreaks += max(sequenceLengths) >= 6
print("Chance of streak: %s%%" % (numberOfStreaks / 100))
