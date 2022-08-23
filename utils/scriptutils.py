import yaml
from yaml.loader import SafeLoader
import subprocess as sbp

def launchScript(args: list) -> str:
    """
    Accepts a list of arguments,
    first being the path of the script
    Launches a script and returns the output
    """
    return sbp.run([" ".join(map(str, args))], stdout=sbp.PIPE, shell=True).stdout.decode("UTF-8").strip()

def launchScriptInNewShell(arg: str, launchInTmux=False) -> None:
    sbp.Popen(f"gnome-terminal -- bash -c '{arg}; exec bash'", shell=True)
    if launchInTmux is True:
        raise "Tmux integration not implemented yet"

def parseScriptsFromYaml(path: str) -> dict:
    data = dict()
    stream = open(path, "r")
    data = yaml.load(stream, Loader=SafeLoader)
    stream.close()
    return data
