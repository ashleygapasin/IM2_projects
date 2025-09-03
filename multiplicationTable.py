while True:
    rows = int(input("Enter rows: "))
    columns = int(input("Enter columns: "))

    if rows == 0 or columns == 0:
        print()
        print("Enter another number for rows or columns")
        break

    search = int(input("Search: "))

    for x in range(1, rows + 1):
        for y in range(1, columns + 1):
            value = x * y
            if value == search:
                print(f"[{value}]", end="\t")
            else:
                print(value, end="\t")
        print()
    break