import argparse
from utils.parsing import ParsedSettings
from utils.scriptutils import parseScriptsFromJSON
from windows.mainwindow import openWindow

class Program:
    script_manager: ParsedSettings
    scripts: dict[str, str]
    scenarios: dict[str, dict]
    args: argparse.Namespace

    def __init__(self, jsonPath=None) -> None:
        self.script_manager = ParsedSettings()
        self.args = self.script_manager.parse()
        if jsonPath == None:
            d, _ = parseScriptsFromJSON(self.args.c)
            self.reloadScriptsData(d)
            openWindow(list(self.scripts.keys()))
        else:
            d, _ = parseScriptsFromJSON(jsonPath)
            self.reloadScriptsData(d)


    def reloadScriptsData(self, data: dict):
        self.scripts = data["scripts"]
        self.scenarios = data["scenarios"]

    def getScenarios(self):
        return self.scenarios

    def getScriptPaths(self):
        return self.scripts

    def getScriptPath(self, scriptNameIn: str):
        for scriptName, scriptPath in self.scripts.items():
            if scriptNameIn == scriptName:
                return scriptPath
        return ""

    def getJSONFile(self):
        return self.args.c
