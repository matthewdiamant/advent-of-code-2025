import unittest

def validate_id_1(id):
    str_id = str(id)
    if len(str_id) % 2 != 0:
        return True
    id_len = len(str_id) / 2
    first_half = str_id[:int(id_len)]
    second_half = str_id[int(id_len):]
    return first_half != second_half

def validate_id_2(id):
    str_id = str(id)
    for n in range(1, len(str_id)):
        if len(str_id) / n % 1 == 0:
            groups = {}
            for i, c in enumerate(str_id):
                index = i // n
                groups[index] = groups[index] if index in groups else ""
                groups[index] = groups[index] + c
            values = list(groups.values())
            if all(values[0] == other for other in values):
                return False
    return True

def range_score_1(r):
    score = 0
    for id in range(r[0], r[1] + 1):
        if not validate_id_1(id):
            score += id
    return score

def range_score_2(r):
    score = 0
    for id in range(r[0], r[1] + 1):
        if not validate_id_2(id):
            score += id
    return score

def solve_1(input):
    ranges = [list(map(int, line.split('-'))) for line in input.split(",")]
    invalid_id_sum = 0
    for r in ranges:
        invalid_id_sum += range_score_1(r)
    return invalid_id_sum

def solve_2(input):
    ranges = [list(map(int, line.split('-'))) for line in input.split(",")]
    invalid_id_sum = 0
    for r in ranges:
        invalid_id_sum += range_score_2(r)
    return invalid_id_sum

with open("./example.txt") as f: example = f.read()
with open("./input.txt")   as f: input   = f.read()

class Test(unittest.TestCase):
    def test_solve_example_1(self):
        self.assertEqual(solve_1(example), 1227775554)

    def test_solve_1(self):
        self.assertEqual(solve_1(input), 35367539282)

    def test_solve_example_2(self):
        self.assertEqual(solve_2(example), 4174379265)

    def test_solve_2(self):
        self.assertEqual(solve_2(input), 45814076230)

unittest.main()
