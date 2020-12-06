from typing import List
import re

def get_input(file: str) -> List[str]:
    with open(file, 'r') as f:
        passports = f.read().split('\n\n')

        for passport in passports:
            passports[passports.index(passport)] = passport.replace(' ', '\n')
        
        return passports


def count_part_1(passports: List[str]) -> int:
    count = 0

    for passport in passports:
        required_fields = [
            'byr',
            'iyr',
            'eyr',
            'hgt',
            'hcl',
            'ecl',
            'pid'
        ]

        for field in passport.split('\n'):
            key = field.split(':')[0]

            if key in required_fields:
                del required_fields[required_fields.index(key)]

        if len(required_fields) == 0:
            count += 1

        else:
            pass
    
    return count


def count_part_2(passports: List[str]) -> int:
    count = 0

    patterns = [
        r'byr:(19[2-9][0-9]|200[0-2])',
        r'iyr:(201[0-9]|2020)',
        r'eyr:(202[0-9]|2030)',
        r'hgt:(?:(?:1[5-8][0-9]|19[0-3])cm|(?:59|6[0-9]|7[0-6])in)\b',
        r'hcl:(#[a-f0-9]{6})\b',
        r'ecl:(amb|blu|brn|gry|grn|hzl|oth)\b',
        r'pid:([0-9]{9})\b'
    ]

    for passport in passports:
        for pattern in patterns:
            if not re.search(pattern, passport):
                break
        
        else:
            count += 1
    
    return count


if __name__ == "__main__":
    passports = get_input('input.txt')

    count_1 = count_part_1(passports)
    count_2 = count_part_2(passports)
            
    print(count_1)
    print(count_2)
