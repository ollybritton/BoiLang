def find_brackets(array):
    bracketPositions = []
    brackets = []
    for i, item in enumerate(array):
        if i == 0 and item == 'boie':
            print("Non sense ! Exit")
            break

        if item == 'bois':
            bracketPositions.append(i)
        elif item =='boie':
            if len(bracketPositions) > 0:
                openingPosition = bracketPositions.pop()
                brackets.append([openingPosition, i])

    return brackets
