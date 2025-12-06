import unittest

def validate_id(id):
    str_id = str(id)
    if len(str_id) % 2 != 0:
        return True
    id_len = len(str_id) / 2
    first_half = str_id[:int(id_len)]
    second_half = str_id[int(id_len):]
    return first_half != second_half


def range_score(r):
    score = 0
    for id in range(r[0], r[1] + 1):
        if not validate_id(id):
            score += id
    return score

def solve_1(input):
    ranges = [list(map(int, line.split('-'))) for line in input.split(",")]
    invalid_id_sum = 0
    for r in ranges:
        invalid_id_sum += range_score(r)
    return invalid_id_sum

def solve_2(input):
    return input

with open("./example.txt") as f: example = f.read()
with open("./input.txt")   as f: input   = f.read()

class Test(unittest.TestCase):
    def test_solve_example_1(self):
        self.assertEqual(solve_1(example), 1227775554)

    def test_solve_1(self):
        self.assertEqual(solve_1(input), None)

    def test_solve_example_2(self):
        return
        self.assertEqual(solve_2(example), None)

    def test_solve_2(self):
        return
        self.assertEqual(solve_2(input), None)

unittest.main()
