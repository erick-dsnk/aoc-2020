

def get_input(file):
    with open(file, 'r') as f:
        return f.read().split('\n')


def parse_input(data, index):
    line = data[index]

    line = line.split(' ')

    occurences = line[0]

    lowest_number = int(occurences.split('-')[0])
    highest_number = int(occurences.split('-')[1])
    char = line[1].strip(':')
    password = line[2]

    return lowest_number, highest_number, char, password


def check_part_1():
    data = get_input('input.txt')

    count = 0

    for i in range(0, len(data) - 1):
        lowest_number, highest_number, char, password = parse_input(data, i)

        n_occurences = password.count(char)

        if n_occurences < lowest_number or n_occurences > highest_number:
            pass
            
        else:
            count += 1
    
    print(f'[part 1] Number of good passwords: {count}')


def check_part_2():
    data = get_input('input.txt')

    count = 0

    for line in data:
        min_max, letter_colon, password = line.split()
        pmin, pmax = [int(c) for c in min_max.split('-')]
        letter = letter_colon[0:1]

        matching_chars = 0

        if password[pmin - 1] == letter:
            matching_chars += 1

        if password[pmax - 1] == letter:
            matching_chars += 1

        if matching_chars == 1:
            count += 1
    
    print(f'[part 2] Number of good passwords: {count}')



if __name__ == "__main__":
    check_part_1()
    check_part_2()