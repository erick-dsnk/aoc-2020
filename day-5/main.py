from typing import List


def get_input(file='input.txt') -> List[str]:
    with open(file, 'r') as f:
        return f.read().split('\n')


def get_ids(data: List[str]) -> int:
    ids = []

    for bpass in data:
        row_exp = bpass[0:7]
        col_exp = bpass[7:10]

        row_range = [i for i in range(128)]
        col_range = [i for i in range(8)]

        for i in range(7):
            if row_exp[i] == 'F':
                row_range = row_range[ 0:(len(row_range) // 2) ]
            
            elif row_exp[i] == 'B':
                row_range = row_range[ (len(row_range) // 2):(len(row_range)) ]
        
        row = row_range[0]

        for i in range(3):
            if col_exp[i] == 'L':
                col_range = col_range[ 0:(len(col_range) // 2) ]

            elif col_exp[i] == 'R':
                col_range = col_range[ (len(col_range) // 2):(len(col_range)) ]

        col = col_range[0]

        seat_id = row * 8 + col

        ids.append(seat_id)
    
    return ids



def get_my_id(ids: List[int]):
    lowest_id = min(ids)

    length = len(ids) + 1

    return (length * (length - 1) // 2 + length * lowest_id - sum(ids))



if __name__ == "__main__":
    data = get_input()

    ids = get_ids(data)

    print(max(ids)) # part 1
    print(get_my_id(ids)) # part 2
