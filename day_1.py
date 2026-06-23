#make a pixel cat

cat_matrix = [
    [0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 2, 1, 1, 1, 2, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 3, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [4, 1, 1, 1, 1, 1, 1, 1, 4, 0, 0, 0, 0, 0],
    [4, 1, 1, 1, 1, 1, 1, 1, 4, 0, 0, 0, 0, 0],
    [4, 1, 1, 1, 1, 1, 1, 1, 4, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 5, 1, 1, 1, 6],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 4, 4, 0, 4, 4, 0, 0, 0, 0, 0, 0, 0]
]

for row in cat_matrix:
    for pixel in row:
        if pixel == 0:
            print(" ", end="")
        elif pixel == 1:
            print("*", end="")
        elif pixel == 2:
            print("o", end="")
        elif pixel == 3:
            print("^", end="")
        elif pixel == 4:
            print("#", end="")
        elif pixel == 5:
            print("<", end="")
        elif pixel == 6:
            print(">", end="")
    print()


print("https://youtube.com/shorts/RVqg5uPVzrQ?si=8FOqIMJ-tkO9gJ27")

