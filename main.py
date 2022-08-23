import yaml
import argparse as ag
from yaml.loader import SafeLoader
import subprocess

from utils.scriptutils import readScriptOutput
# from windows.mainwindow import openWindow

out = readScriptOutput("~")

def main():
    parser = ag.ArgumentParser(conflict_handler="resolve", usage="\n", formatter_class=ag.RawTextHelpFormatter)
    parser.add_argument("-c", metavar="stats", required=True, help="Yaml config path string")
    out = readScriptOutput(["./script", 1000])
    print(out)

if __name__ == "__main__":
    main()
