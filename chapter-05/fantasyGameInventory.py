stuff = {
    "rope": 1,
    "torch": 6,
    "gold coin": 42,
    "dagger": 1,
    "arrow": 12,
}


dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]


def displayInventory(inventory: dict) -> None:
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(f"{v} {k}")
        item_total += v
    print("Total number of items: " + str(item_total))


def addToInventory(inventory: dict, addedItems: list) -> dict:
    for item in addedItems:
        inventory[item] = inventory.get(item, 0)
        inventory[item] += 1


displayInventory(stuff)
addToInventory(stuff, dragonLoot)
displayInventory(stuff)
