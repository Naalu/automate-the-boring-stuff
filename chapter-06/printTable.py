def printTable(data: list) -> None:
    """Prints data (list of lists)
    in a nicely formatted table"""

    colWidths = [0] * len(data)
    for idx, width in enumerate(colWidths):
        longest = 0
        for word in data[idx]:
            longest = max(longest, len(word))
        colWidths[idx] = longest
    for i in range(len(data[0])):
        for idx, word in enumerate(data):
            print(data[idx][i].rjust(colWidths[idx]), end=" ")
        print()

    return None


tableData = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "moose", "goose"],
]

printTable(tableData)
