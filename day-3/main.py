def get_input(file: str) -> str:
    with open(file, 'r') as f:
        return f.read().split('\n')


def count(data: list, x_slope: int, y_slope: int = 1):
    x = x_slope
    y = y_slope

    n = 0

    finished = False

    while not finished:
        if y > len(data) - 1:
            finished = True
            break
        
        if x >= len(data[y]):
            x -= len(data[y])

        if data[y][x] == '#':
            n += 1
        
        x += x_slope
        y += y_slope
    
    return n


if __name__ == "__main__":
    data = get_input('input.txt')

    slope_1 = count(data, 1)
    slope_2 = count(data, 3)
    slope_3 = count(data, 5)
    slope_4 = count(data, 7)
    slope_5 = count(data, 1, 2)

    print(slope_1, slope_2, slope_3, slope_4, slope_5)

    n = slope_1 * slope_2 * slope_3 * slope_4 * slope_5

    print(n)
