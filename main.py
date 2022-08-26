import json
from program import Program
import utils.parsing
from utils.scriptutils import launchScriptInNewShell, parseScriptsFromJSON, parseScriptsFromYaml
from windows.mainwindow import openWindow

def main():
    d, s = parseScriptsFromJSON("./json/sc.json")

    if True:
        program = Program()
        # scripts = data["scenarios"]["paths"]
        scripts = d["scripts"].values()

        # Launch TUI frontend if the flag is set to true
        # if args.t is False:
        #     openWindow(scripts)
        # else:
        #     launchScriptInNewShell(scripts[0])

    scenarios = d["scenarios"]

    for sc, _ in scenarios.items():
        for script in scenarios[sc]["scripts"]:
            print(script, end=" ")
            for arg in scenarios[sc]["arguments"][script]:
                print(arg, end=" ")
            print()

if __name__ == "__main__":
    main()
