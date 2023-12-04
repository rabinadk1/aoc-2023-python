"""
Your calculation isn't quite right.
It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line.
For example:

```
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
```

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76.
Adding these together produces 281.

What is the sum of all of the calibration values?

Your puzzle answer was 55358.
"""


class DigitTracker:
    def __init__(self):
        # Empty initialization
        self.first_digit = None
        self.second_digit = None

    def update_dgts(self, digit: int):
        if self.first_digit is None:
            self.first_digit = digit
        # Update both digits even if only one number present
        self.second_digit = digit

    def get_sum(self):
        return self.first_digit * 10 + self.second_digit


dgt_literals = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")


def get_sum(inp: str):
    total_sum = 0
    inp_list = inp.splitlines()

    for line in inp_list:
        dgt_tracker = DigitTracker()
        for char_idx, char in enumerate(line):
            # Since the text only contains lower case strings or numerals,
            # checking for lowercase here
            if char.islower():
                # The literals start with one so starting the lit_idx with 1
                for dgt_lit_idx, dgt_lit in enumerate(dgt_literals, 1):
                    if line.startswith(dgt_lit, char_idx):
                        dgt_tracker.update_dgts(dgt_lit_idx)
                        break
            else:
                dgt_tracker.update_dgts(int(char))

        total_sum += dgt_tracker.get_sum()

    return total_sum


if __name__ == "__main__":
    import sys

    args_with_source_code = sys.argv

    if len(args_with_source_code) != 2:
        # For python solution.py
        print("Enter a input filename as the next argument.")
        exit(1)

    filename = args_with_source_code[1]

    with open(filename) as f:
        inp = f.read()

    total_sum = get_sum(inp)

    print("The total sum is:", total_sum)
