import subprocess as sbp

def launchScript(args: list) -> str:
    """
    Accepts a list of arguments,
    first being the path of the script
    Launches a script and returns the output
    """
    return sbp.run([" ".join(map(str, args))], stdout=sbp.PIPE, shell=True).stdout.decode("UTF-8").strip()
