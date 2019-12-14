import json

TEST_CASE_DIR = 'test_cases/'


def read_testing_json(filename):
    with open(TEST_CASE_DIR + filename) as json_file:
        return json_file.read()


def load_testing_json(filename):
    with open(TEST_CASE_DIR + filename) as json_file:
        return json.loads(json_file.read())
