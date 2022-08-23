import subprocess as sbp

def readScriptOutput(args: list) -> str:
    return sbp.run([" ".join(map(str, args))], stdout=sbp.PIPE, shell=True).stdout.decode("UTF-8").strip()
