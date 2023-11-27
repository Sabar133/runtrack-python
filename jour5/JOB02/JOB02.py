def Rectangle(width, height):
    print('-' * width)

    for _ in range(height - 2):
        print('|' + ' ' * (width - 2) + '|')

    if height > 1:
        print('-' * width)

Rectangle(10, 3)
