raw_img = [
    [15, 20, 25, 30, 35],
    [40, 45, 50, 55, 60],
    [65, 70, 75, 80, 85],
    [90, 95, 100, 105, 110]
]

for row in raw_img:
    for pixel in row:
        if pixel <= 60:
            print(0, end=" ")
        else:
            print(pixel, end=" ")
    print()

    