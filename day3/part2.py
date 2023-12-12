"""The missing part wasn't the only issue - one of the gears in the engine is wrong.
A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

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

In this schematic, there are two gears.
The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345.
The second gear is in the lower right; its gear ratio is 451490.
(The * adjacent to 617 is not a gear because it is only adjacent to one part number.)
Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?
"""

from collections import defaultdict
from typing import Sequence

star_num_list = defaultdict(list)


def iterate_top_row(
    schematic_list: Sequence[str],
    line_idx: int,
    char_idx: int,
    clipped_leftmost_idx: int,
    num: int,
) -> None:
    upper_idx = line_idx - 1

    if upper_idx < 0:
        return

    prev_line = schematic_list[upper_idx]

    # char_idx to char_idx - len(num_list) - 1
    for idx in range(clipped_leftmost_idx, char_idx + 1):
        curr_char = prev_line[idx]

        if curr_char == "*":
            star_num_list[(upper_idx, idx)].append(num)


def iterate_bottom_row(
    schematic_list: Sequence[str],
    line_idx: int,
    char_idx: int,
    clipped_leftmost_idx: int,
    num: int,
) -> None:
    next_idx = line_idx + 1

    if next_idx >= len(schematic_list):
        return

    next_line = schematic_list[next_idx]

    # char_idx to char_idx - len(num_list) - 1
    for idx in range(clipped_leftmost_idx, char_idx + 1):
        curr_char = next_line[idx]

        if curr_char == "*":
            star_num_list[(next_idx, idx)].append(num)


def iterate_all_adj(
    curr_char: str,
    num: int,
    char_idx: int,
    num_digits: int,
    curr_line: str,
    schematic_list: Sequence[str],
    line_idx: int,
) -> None:
    if curr_char == "*":
        star_num_list[(line_idx, char_idx)].append(num)

    leftmost_idx = char_idx - num_digits - 1

    # Prev adjacency
    if leftmost_idx >= 0:
        left_char = curr_line[leftmost_idx]

        if left_char == "*":
            star_num_list[(line_idx, leftmost_idx)].append(num)

    clipped_leftmost_idx = max(leftmost_idx, 0)

    args = schematic_list, line_idx, char_idx, clipped_leftmost_idx, num

    iterate_top_row(*args)

    iterate_bottom_row(*args)


def get_gear_ratio_sum(schematic: str):
    schematic_list = schematic.splitlines()

    for line_idx, curr_line in enumerate(schematic_list):
        num_list = []

        # To supress out of bound warning in the else portion
        char_idx = 0
        curr_char = ""

        for char_idx, curr_char in enumerate(curr_line):
            if curr_char.isnumeric():
                num_list.append(curr_char)
            elif len(num_list) != 0:
                num = int("".join(num_list))

                iterate_all_adj(
                    curr_char,
                    num,
                    char_idx,
                    len(num_list),
                    curr_line,
                    schematic_list,
                    line_idx,
                )

                # Start a new number list
                num_list = []

        # The last char in the line may be number
        else:
            if len(num_list) != 0:
                num = int("".join(num_list))

                iterate_all_adj(
                    curr_char,
                    num,
                    char_idx,
                    len(num_list),
                    curr_line,
                    schematic_list,
                    line_idx,
                )

    gear_ratio_sum = 0
    for gear_list in star_num_list.values():
        if len(gear_list) == 2:
            gear_ratio_sum += gear_list[0] * gear_list[1]

    return gear_ratio_sum


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

    total_sum = get_gear_ratio_sum(inp)

    print("The sum of gear ratio is:", total_sum)
