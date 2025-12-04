import unittest

STARTING_POSITION = 50

def solve_1(input):
    instructions = input.split("\n")
    counter = 0
    position = STARTING_POSITION
    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1:])
        if direction == "L":
            position = (position - distance) % 100
        elif direction == "R":
            position = (position + distance) % 100
        if position == 0:
            counter += 1

    return counter

def solve_2(input):
    return input

with open("./example.txt") as f: example = f.read()
with open("./input.txt")   as f: input   = f.read()

class Test(unittest.TestCase):
    def test_solve_example_1(self):
        self.assertEqual(solve_1(example), 3)

    def test_solve_1(self):
        self.assertEqual(solve_1(input), None)

    def test_solve_example_2(self):
        return
        self.assertEqual(solve_2(example), None)

    def test_solve_2(self):
        return
        self.assertEqual(solve_2(input), None)

unittest.main()
