import sys
import argparse
from json import JSONDecodeError
from .nester import Nester


class NesterCli:
    @staticmethod
    def nest():
        parser = argparse.ArgumentParser(description='Groups data from stdin in accordance with passed arguments.')
        parser.add_argument('nested_levels', nargs='*')
        args = parser.parse_args()
        stdin_read = sys.stdin.read()
        try:
            nested = Nester.nest_json(stdin_read, args.nested_levels)
            sys.stdout.write(nested)
        except KeyError as e:
            sys.stderr.write(f"Could not find key: {e}\n")
        except JSONDecodeError as e:
            sys.stderr.write(f"Malformed JSON: {e}\n")
        except ValueError as e:
            sys.stderr.write(f"Inappropriate value: {e}\n")


if __name__ == '__main__':
    NesterCli.nest()
