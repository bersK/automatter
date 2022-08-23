import argparse as ag
import distutils.util as dt

from utils.scriptutils import launchScript, parseScriptsFromYaml
from windows.mainwindow import openWindow

def main():
    parser = ag.ArgumentParser(conflict_handler="resolve", usage="Provide a yaml config, pls", formatter_class=ag.RawTextHelpFormatter)

    parser.add_argument("-c", required=True, type=str, help="Path string to the scripts that will be executed in the program")
    parser.add_argument('-t', default=False, type=lambda x: bool(dt.strtobool(str(x))), help="Choose whether to launc this tool with a TUI frontend or not.")

    args = parser.parse_args()
    print("Path string to the scripts:", args.c)
    print("Should launch TUI:", args.t)


    # test print
    # out = launchScript(["testscripts/script", 1000])
    # print(out)

    data = parseScriptsFromYaml(args.c)

    if args.t is True:
        openWindow(data["scripts"]["paths"])

    print(data)

if __name__ == "__main__":
    main()
