import argparse
from typing import Dict 
from utils.parsing import ParsedSettings
from utils.scriptutils import parseScriptsFromJSON
from windows.mainwindow import openWindow

class Program:
    script_manager: ParsedSettings
    scripts: dict[str, str]
    scenarios: dict[str, dict]
    args: argparse.Namespace

    def __init__(self) -> None:
        self.script_manager = ParsedSettings()
        self.args = self.script_manager.parse()

        d, s = parseScriptsFromJSON(self.args.c)
        self.scripts = d["scripts"]
        self.scenarios = d["scenarios"]
        print(self.scripts)
        openWindow(self.scenarios.keys())

