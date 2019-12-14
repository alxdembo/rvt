import json
import unittest


from .nester import Nester

TEST_CASE_DIR = 'nester/test_cases/'


class NesterTest(unittest.TestCase):
    @staticmethod
    def __load_json(filename):
        with open('nester/test_cases/' + filename) as json_file:
            return json.loads(json_file.read())

    def test_nest(self):
        input_json = 'input/original_task.json'
        output_json = 'output/original_task.json'
        nesting_levels = ['currency', 'country', 'city']

        actual = Nester.nest(self.__load_json(input_json), nesting_levels)
        expected = self.__load_json(output_json)

        self.assertEqual(expected, actual)
