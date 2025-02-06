def split_points(points):
    new_points_list = []

    for x, y in points:
        max_splits = min(abs(x), abs(y)) if x != 0 and y != 0 else 10

        if x == 0 and y == 0:
            new_points_list.append([(0, 0)])
            continue

        step_x = x // max_splits if x != 0 else 0
        step_y = y // max_splits if y != 0 else 0
        remainder_x = x % max_splits if x != 0 else 0
        remainder_y = y % max_splits if y != 0 else 0

        new_points = [(step_x, step_y) for _ in range(max_splits - 1)]
        new_points.append((step_x + remainder_x, step_y + remainder_y))

        new_points_list.append(new_points)

    return new_points_list


# Exemplu de utilizare:
points = [
    (0, 0), (0, 23), (-3, 23), (-7, 23), (-8, 23), (-11, 23), (-13, 22),
    (-13, 23), (-13, 22), (-15, 22), (-15, 23), (-15, 23), (-15, 22),
    (-14, 22), (-15, 22), (-16, 23), (-15, 22), (-14, 23), (-16, 23),
    (-15, 23), (-15, 23), (-15, 24), (-16, 23), (-15, 23), (-14, 23),
    (-16, 23), (-15, 23), (-16, 23), (-15, 22)
]


if __name__ == "__main__":
    for sublist in split_points(points):
        for i in sublist:
            print (f"{i},")