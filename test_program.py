from utils.scriptutils import parseScriptsFromJSON
import json
from program import Program

test_json_path = "json/test_sc.json"
test_scripts = {
    "echocommands": "~/bin/echocommands",
    "syncmaster": "~/bin/syncmaster"
}

# check if it loads the predefined scripts correctly
def program_load_scripts_case():
    program = Program(test_json_path)
    return program.getScriptPaths()

def test_program_loading_scripts():
    script_paths = [path for _, path in program_load_scripts_case().items()]
    test_script_paths = [path for _, path in test_scripts.items()]
    assert script_paths == test_script_paths

# check if it loads the predefined scenarios correctly
def program_load_scenarios_case():
    program = Program(test_json_path)
    return program.getScenarios()

def test_program_load_scenarios():
    scenarios = ["scenario1", "scenario2"]
    loaded_scenarios = program_load_scenarios_case().keys()
    assert scenarios.sort() == list(loaded_scenarios).sort()

def program_reload_scenarios_case():
    program = Program(test_json_path)
    return program.getScenarios()

def test_program_reload_scenarios():
    scenarios = ["scenario1", "scenario2"]
    loaded_scenarios = program_load_scenarios_case().keys()
    assert scenarios.sort() == list(loaded_scenarios).sort()
