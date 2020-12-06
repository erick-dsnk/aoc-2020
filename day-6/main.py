from typing import List

data = [group.split('\n') for group in open('input.txt', 'r').read().split('\n\n')]

def part_1():
    count_sum = 0

    for group in data:
        yes_answers = []

        for person in group:
            for char in person:
                if char in yes_answers:
                    pass
                
                else:
                    yes_answers.append(char)
        
        count_sum += len(yes_answers)

    return count_sum


def part_2():
    count_sum = 0

    for group in data:
        yes_answers = {
            'a': 0,
            'b': 0,
            'c': 0,
            'd': 0,
            'e': 0,
            'f': 0,
            'g': 0,
            'h': 0,
            'i': 0,
            'j': 0,
            'k': 0,
            'l': 0,
            'm': 0,
            'n': 0,
            'o': 0,
            'p': 0,
            'q': 0,
            'r': 0,
            's': 0,
            't': 0,
            'u': 0,
            'v': 0,
            'w': 0,
            'x': 0,
            'y': 0,
            'z': 0
        }

        valid = []

        for person in group:
            for char in person:
                yes_answers[char] += 1
        
        for char, value in yes_answers.items():
            if value == len(group):
                valid.append(char)

        count_sum += len(valid)

    return count_sum


if __name__ == "__main__":
    print(part_1())
    print(part_2())