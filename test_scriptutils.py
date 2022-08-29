from utils.scriptutils import parseScriptsFromJSON

test_scripts = {
    "echocommands": "~/bin/echocommands",
    "syncmaster": "~/bin/syncmaster"
}

# check if the methods loads the scripts data correctly
def parse_scripts_case():
    d, _ = parseScriptsFromJSON("json/sc.json")
    return d["scripts"]

def test_loading_scripts_case():
    scripts = parse_scripts_case()
    assert scripts == test_scripts
