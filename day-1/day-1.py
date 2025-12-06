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
    instructions = input.split("\n")
    counter = 0
    position = STARTING_POSITION

    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1:])
        diff = position - distance if direction == "L" else position + distance
        counter += abs(diff // 100)
        position = diff % 100

    return counter

with open("./example.txt") as f: example = f.read()
with open("./input.txt")   as f: input   = f.read()

class Test(unittest.TestCase):
    def test_solve_example_1(self):
        self.assertEqual(solve_1(example), 3)

    def test_solve_1(self):
        self.assertEqual(solve_1(input), 999)

    def test_solve_example_2(self):
        self.assertEqual(solve_2(example), 6)

    def test_solve_2(self):
        self.assertEqual(solve_2(input), 6099)

unittest.main()
