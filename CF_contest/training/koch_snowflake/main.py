"""Get the perimeter of a Koch Snowflake generated after n iterations
made of equilateral squares/triangles of length m"""

import argparse


class KochSnowflake:

    init_sides = {"tri": 3, "sq": 4}
    side_multiplier = {"tri": 4, "sq": 5}

    def __init__(self, type, length, iterations):
        assert length > 0 and iterations >= 0, "wrong input"

        self.type = type
        self.length = length
        self.iterations = iterations

        self.perimeter = 0

        self.spawn_snowflake()

    def spawn_snowflake(self):

        # get initial triangle
        current_length = self.length
        sides = self.init_sides[self.type]
        for i in range(self.iterations):
            sides *= self.side_multiplier[self.type]
            current_length /= 3
        self.perimeter = sides * current_length

    def get_perimeter(self):
        return self.perimeter


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", choices=["tri", "sq"], required=True)
    parser.add_argument("--length", type=int, required=True)
    parser.add_argument("--iterations", type=int, required=True)

    args = parser.parse_args()

    flake = KochSnowflake(args.type, args.length, args.iterations)
    print(f"Perimeter of the flake (length: {args.length}, iterations: {args.iterations}) is {flake.get_perimeter()}")
