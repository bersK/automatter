from dataclasses import dataclass
from utils.parsing import ParsedSettings
from utils.scriptutils import launchScriptInNewShell, parseScriptsFromYaml
from windows.mainwindow import openWindow

# @dataclass
# class Program:
#     pass

def main():
    args = ParsedSettings.parse()
    # print("Path string to the scripts:", args.c)
    # print("Should launch TUI:", args.t)

    data = parseScriptsFromYaml(args.c)
    scripts = data["scenarios"]["paths"]

    # Launch TUI frontend if the flag is set to true
    if args.t is True:
        openWindow(scripts)
    else:
        launchScriptInNewShell(scripts[0])

if __name__ == "__main__":
    main()
