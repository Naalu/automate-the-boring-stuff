def printTable(data: list) -> None:
    """Prints data (list of lists)
    in a nicely formatted table"""

    colWidths = [0] * len(data)
    for idx, row in enumerate(data):
        colWidths[idx] = max([len(word) for word in row])

    newTable = {}
    for i in range(len(data)):
        for j in range(len(data[0])):
            newTable[j] = newTable.get(j, [])
            newTable[j].append(data[i][j].rjust(colWidths[i]))

    for k, v in newTable.items():
        newTable[k] = " ".join(v)
        print(newTable[k])

    return None


tableData = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "moose", "goose"],
]

printTable(tableData)
