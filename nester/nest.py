import json
import sys
import argparse
from json import JSONDecodeError

from nester import Nester


class NesterCli:
    @staticmethod
    def nest():
        parser = argparse.ArgumentParser(
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description='''
Groups data from stdin in accordance with passed arguments.
Example:

        cat test_cases/input/original_task.json  | python3 nest.py currency country city''')

        parser.add_argument('nested_levels', nargs='*', help='Arbitrary number of nesting levels separated with space.')
        args = parser.parse_args()
        stdin_read = json.loads(sys.stdin.read())
        try:
            nested = Nester.nest(stdin_read, args.nested_levels)
            sys.stdout.write(json.dumps(nested, indent=2, sort_keys=True))
        except KeyError as e:
            sys.stderr.write(f"Could not find key: {e}\n")
        except JSONDecodeError as e:
            sys.stderr.write(f"Malformed JSON: {e}\n")
        except ValueError as e:
            sys.stderr.write(f"Inappropriate value: {e}\n")


if __name__ == '__main__':
    NesterCli.nest()
