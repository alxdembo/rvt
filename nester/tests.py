import json
import sys
import unittest
import io
from unittest.mock import patch

from helpers.test_helpers import load_testing_json, read_testing_json, TEST_CASE_DIR
from .nester import Nester
from .nest import NesterCli


class NesterTest(unittest.TestCase):
    def test_nest(self):
        input_json = 'input/original_task.json'
        output_json = 'output/original_task.json'
        nesting_levels = ['currency', 'country', 'city']

        actual = Nester.nest(load_testing_json(input_json), nesting_levels)
        expected = load_testing_json(output_json)

        self.assertEqual(expected, actual)

    def test_nest_raises_invalid_key_error(self):
        input_json = 'input/original_task.json'
        nesting_levels = ['123']

        self.assertRaises(KeyError, Nester.nest, load_testing_json(input_json), nesting_levels)

    def test_nest_raises_invalid_value_error(self):
        input_json = 'invalid json'
        nesting_levels = ['123']

        self.assertRaises(ValueError, Nester.nest_json, input_json, nesting_levels)

        # passing invalid nesting levels
        input_json = '{"valid":"json"}'
        nesting_levels = []

        self.assertRaises(ValueError, Nester.nest_json, input_json, nesting_levels)

    def test_nest_json(self):
        input_json = 'input/original_task.json'
        output_json = 'output/original_task.json'
        nesting_levels = ['currency', 'country', 'city']

        actual = json.loads(Nester.nest_json(read_testing_json(input_json), nesting_levels))
        expected = load_testing_json(output_json)

        self.assertEqual(expected, actual)

    def test_nest_cli(self):
        input_json = 'input/original_task.json'
        output_json = 'output/original_task.json'

        sys.argv = ['', 'currency', 'country', 'city']
        sys.stdin = open(TEST_CASE_DIR + input_json, 'r')

        with patch('sys.stdout', new=io.StringIO()) as output:
            NesterCli.nest()
        actual = json.loads(output.getvalue().strip())

        read_json_output = read_testing_json(output_json)
        expected = json.loads(read_json_output)

        self.assertEqual(expected, actual)
