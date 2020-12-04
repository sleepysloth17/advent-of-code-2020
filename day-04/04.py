from typing import Generator, List, Set, Dict, Callable, KeysView, Pattern
from re import compile

INPUT_FILE_NAME: str = "day-04-input.txt"

INCLUDE_FOR_VALID: Set[str] = set(
    [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
        # 'cid', don't need this; is optional
    ]
)

HAIR_REGEX: Pattern = compile("^#[a-f\\d]{6}$")

HEIGHT_REGEX: Pattern = compile("^\\d{2,3}(?:in|cm)$")

CONDITION_DICT: Dict[str, Callable[[str], bool]] = {
    "byr": lambda s: s.isdigit() and 1920 <= int(s) <= 2002,
    "iyr": lambda s: s.isdigit() and 2010 <= int(s) <= 2020,
    "eyr": lambda s: s.isdigit() and 2020 <= int(s) <= 2030,
    "hgt": lambda s: bool(HEIGHT_REGEX.match(s))
    and ((150 <= int(s[:-2]) <= 193) if s[-2:] == "cm" else (59 <= int(s[:-2]) <= 76)),
    "hcl": lambda s: bool(HAIR_REGEX.match(s)),
    "ecl": lambda s: s in set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]),
    "pid": lambda s: s.isdigit() and len(s) == 9,
    "cid": lambda s: True,
}


def get_input_list() -> Generator[Dict[str, str], None, None]:
    with open(INPUT_FILE_NAME) as input_file:
        single_passport: List[str] = []
        for line in input_file:
            new_entries = line.strip().split()
            if not len(new_entries):
                yield get_dict(single_passport)
                single_passport = []
            else:
                single_passport = single_passport + new_entries
        yield get_dict(single_passport)


def get_dict(passport_list: List[str]) -> Dict[str, str]:
    return_dict: Dict[str, str] = {}

    for field in passport_list:
        split_field: List[str] = field.split(":")
        return_dict[split_field[0]] = split_field[1]

    return return_dict


def count_valid() -> int:
    count: int = 0
    for passport in get_input_list():
        if validate(passport):
            count += 1
    return count


def validate(passport: Dict[str, str]) -> bool:
    if not INCLUDE_FOR_VALID.issubset(passport.keys()):
        return False
    for item in passport.items():
        if not CONDITION_DICT[item[0]](item[1]):
            return False
    return True


if __name__ == "__main__":
    print("result: ", count_valid())
