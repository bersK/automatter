import argparse
import distutils.util as dt
from dataclasses import dataclass

@dataclass
class ParsedSettings:
    # self.args: argparse.Namespace
    def parse():
        parser = argparse.ArgumentParser(conflict_handler="resolve", usage="Provide a yaml config, pls", formatter_class=argparse.RawTextHelpFormatter)

        parser.add_argument("-c", required=True, type=str, help="Path string to the scripts that will be executed in the program")
        parser.add_argument('-t', default=False, type=lambda x: bool(dt.strtobool(str(x))), help="Choose whether to launc this tool with a TUI frontend or not.")

        return parser.parse_args()
