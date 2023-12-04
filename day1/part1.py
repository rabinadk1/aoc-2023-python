"""
On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.
For example:

```
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
```

In this example, the calibration values of these four lines are 12, 38, 15, and 77.
Adding these together produces 142.

Consider your entire calibration document.
What is the sum of all of the calibration values?

Your puzzle answer was 56042.
"""


def get_sum(inp: str):
    total_sum = 0
    inp_list = inp.splitlines()

    for line in inp_list:
        first_char = None
        second_char = None
        for char in line:
            # Since the text only contains lower case strings or numerals,
            # checking for lowercase here
            if not char.islower():
                if first_char is None:
                    first_char = char
                second_char = char

        # Adding chars and converting them to int works since the numbers are of single digit.
        total_sum += int(first_char + second_char)

    return total_sum


if __name__ == "__main__":
    import sys

    args_with_source_code = sys.argv

    if len(args_with_source_code) != 2:
        # For `python solution.py`, there is one arg.
        print("Enter a input filename as the next argument.")
        exit(1)

    filename = args_with_source_code[1]

    with open(filename) as f:
        inp = f.read()

    total_sum = get_sum(inp)

    print("The total sum is:", total_sum)
