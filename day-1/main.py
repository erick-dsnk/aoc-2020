

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

def check_iteration_2(data): # a bit of a brute force solution but couldn't think of a solution similar to part 1
    for i in data:
        for j in data:
            for k in data:
                if i + j + k == 2020:
                    print(f'[!] Found numbers that add up to 2020: `{i}` `{j}` `{k}`')

                    return i, j, k
