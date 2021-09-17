with open("numbers", "w") as file:
    numbers = []
    for i in range(0, 1338):
        numbers.append(str(i) + "\n")

    file.writelines(numbers)
