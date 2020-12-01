from timeit import Timer

def get_input(filename: str):
    print(f"[*] Opening '{filename}'...")

    with open(filename, 'r') as f:
        data = f.read()

    print("[*] Acquired input data.")

    return [int(i) for i in data.split('\n')]

def check_iteration_1(data, index):
    print(f'[*] Checking iteration starting from index: i = {index}')

    for i in data[index:(len(data) - 1)]:
        if data[index] + i == 2020:
            print(f'[!] Found numbers that add up to 2020: `{data[index]}` `{i}`')
            
            return data[index], i
    
    check_iteration_1(data, index + 1)

def check_iteration_2(data, index):
    print(f'[*] Checking iteration starting from index: i = {index}')

    for i in data[index:(len(data) - 1)]:
        for j in data[(index + 1):(len(data) - 1)]:
            if i + j + data[index] == 2020:
                print(f'[!] Found numbers that add up to 2020: `{i}` `{j}` `{data[index]}`')

                return i, j, data[index]

    check_iteration_2(data, index + 1)


if __name__ == "__main__":
    data = get_input('input.txt')

    start = Timer()
    pair_of_3 = check_iteration_2(data, 0)
    end = Timer()

    print(end - start)
