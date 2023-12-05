"""The engine schematic (your puzzle input) consists of a visual representation of the engine.
There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum.
(Periods (.) do not count as a symbol.).

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right).
Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger.
What is the sum of all of the part numbers in the engine schematic?
"""
from typing import Sequence


def is_symbol(char: str) -> bool:
    return not (char == "." or char.isnumeric())


def get_is_top_adj(
    schematic_list: Sequence[str],
    line_idx: int,
    char_idx: int,
    clipped_leftmost_idx: int,
):
    upper_idx = line_idx - 1

    if upper_idx < 0:
        return False

    prev_line = schematic_list[upper_idx]
    # char_idx to char_idx - len(num_list) - 1
    return any(
        is_symbol(prev_line[idx]) for idx in range(clipped_leftmost_idx, char_idx + 1)
    )


def get_is_bottom_adj(
    schematic_list: Sequence[str],
    line_idx: int,
    char_idx: int,
    clipped_leftmost_idx: int,
):
    next_idx = line_idx + 1

    if next_idx >= len(schematic_list):
        return False

    next_line = schematic_list[next_idx]
    return any(
        is_symbol(next_line[idx]) for idx in range(clipped_leftmost_idx, char_idx + 1)
    )


def get_is_adj(
    curr_char: str,
    char_idx: int,
    num_digits: int,
    curr_line: str,
    schematic_list: Sequence[str],
    line_idx: int,
):
    # Next adjacency
    if is_symbol(curr_char):
        return True

    leftmost_idx = char_idx - num_digits - 1

    # Prev adjacency
    if leftmost_idx >= 0 and is_symbol(curr_line[leftmost_idx]):
        return True

    clipped_leftmost_idx = max(leftmost_idx, 0)

    args = schematic_list, line_idx, char_idx, clipped_leftmost_idx

    if get_is_top_adj(*args):
        return True

    return get_is_bottom_adj(*args)


def get_engine_sum(schematic: str):
    engine_sum = 0
    schematic_list = schematic.splitlines()

    for line_idx, curr_line in enumerate(schematic_list):
        num_list = []
        for char_idx, curr_char in enumerate(curr_line):
            if curr_char.isnumeric():
                num_list.append(curr_char)
            elif len(num_list) != 0:
                num = int("".join(num_list))

                if get_is_adj(
                    curr_char,
                    char_idx,
                    len(num_list),
                    curr_line,
                    schematic_list,
                    line_idx,
                ):
                    engine_sum += num

                # Start a new number list
                num_list = []

        # The last char in the line may be number
        else:
            if len(num_list) != 0:
                num = int("".join(num_list))

                if get_is_adj(
                    curr_char,
                    char_idx,
                    len(num_list),
                    curr_line,
                    schematic_list,
                    line_idx,
                ):
                    engine_sum += num

    return engine_sum


if __name__ == "__main__":
    import sys

    args_with_source_code = sys.argv

    if len(args_with_source_code) != 2:
        # For python solution.py
        print("Enter a input filename as the next argument.")
        sys.exit(1)

    filename = args_with_source_code[1]

    with open(filename) as f:
        inp = f.read()

    total_sum = get_engine_sum(inp)

    print("The total sum is:", total_sum)
