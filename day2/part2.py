"""
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

- In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes.
    If any color had even one fewer cube, the game would have been impossible.
- Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
- Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
- Game 4 required at least 14 red, 3 green, and 15 blue cubes.
- Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.

The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together.
The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively.
Adding up these five powers produces the sum 2286.

For each game, find the minimum set of cubes that must have been present.
What is the sum of the power of these sets?
"""

def get_sum_ids(game_inp: str):
    sum_power = 0
    inp_list = game_inp.splitlines()

    for line in inp_list:
        # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        game, revelations = line.split(":", maxsplit=1)

        # ["3 blue, 4 red", "1 red, 2 green, 6 blue", "2 green"]
        max_rev_dict: dict[str, int] = {}

        # rev is in this format: 3 blue, 4 red
        for rev in revelations.split(";"):
            for num_color in rev.split(","):
                # There could be space after comma so using left strip
                # ["3", "blue"]
                str_num, color = num_color.lstrip().split(" ", maxsplit=1)

                int_num = int(str_num)
                
                max_rev_dict[color] = max(int_num, max_rev_dict.get(color, 0))

        power = 1
        for max_num in max_rev_dict.values():
            power *= max_num
        
        sum_power += power
    
    return sum_power

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

    total_sum = get_sum_ids(inp)

    print("The total sum is:", total_sum)
