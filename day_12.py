# Format: [x_min, y_min, x_max, y_max]
bounding_boxes = [
    [10, 20, 50, 80],   # Valid
    [40, 50, 30, 80],   # Invalid (x_min is 40, but x_max is 30!)
    [0, 5, 10, 15],     # Valid
    [20, 30, 60, 25]    # Invalid (y_min is 30, but y_max is 25!)
]


valid = []

for box in bounding_boxes:
    x_min, y_min, x_max, y_max = box
    if x_min < x_max and y_min < y_max:
        valid.append(box)

print(valid)