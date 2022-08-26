import argparse
import distutils.util as dt

class ParsedSettings:
    args: argparse.Namespace

    def __init__(self) -> None:
        self.args = argparse.Namespace()

    def parse(self) -> argparse.Namespace:
        parser = argparse.ArgumentParser(conflict_handler="resolve", usage="Provide a yaml config, pls", formatter_class=argparse.RawTextHelpFormatter)

        parser.add_argument("-c", default="./json/sc.json", required=False, type=str, help="Path string to the scripts that will be executed in the program")
        parser.add_argument("-f", default="JSON", required=False, type=str, help="File type of the scenarios file, currently supported - [JSON]")
        parser.add_argument('-t', default=False, type=lambda x: bool(dt.strtobool(str(x))), help="Choose whether to launc this tool with a TUI frontend or not.")

        self.args = parser.parse_args()
        return self.args

    def values(self) -> argparse.Namespace:
        return self.args
