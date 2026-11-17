import os

def cls():
    os.system("clear||cls")

def line():
    print("X+"+"—"*36+"+X")

def organize_options(data: list):
    row = ""
    rows = []

    for number, item in enumerate(data, start = 1):
        item = f"[{number}]. {item}"

        # if another item already exists, it get separeted, if not, the item just gets added
        if row:
            content = row + " | " + item
        else:
             content = item

        # if it exceeded the moldure lenght, it gets a separeted row on the list rows
        if len(content) <= 40:
            row = content
        else:
            rows.append(row)
            row = item

        # if the content dont exceeded the moldure, it gets added to rows
    if row:
        rows.append(row)

    return rows
        

def show(data, mode: str, title):
    match mode:
        case "question":
            line()
            print(title)
            line()

        case "text":
            line()
            for text in title:
                print(text)
            line()
            
        case "options":
            if title:
                line()
                print(title)
            line()
            for row in data:
                print(row)
            line()
