from pytermgui import *
from utils.scriptutils import *
import subprocess as sbp

def submit(args):
    print(" ".join(args))
    # out = launchScript(args)
    launchScriptInNewShell(" ".join(args))

def loadStyleConfig(path: str) -> str:
    fileconfig = open(path, "r")
    yamlStyle = fileconfig.read()
    fileconfig.close()
    return yamlStyle

def loadFields(fields: list) -> Window:
    input_fields = list()
    input_fields.append("")
    for field in fields:
        input_fields.append(InputField(field, prompt="Path: "))
        input_fields.append(["Launch", lambda *_: submit(field)])
    input_fields.append("")

    window = Window(*input_fields, width=80, box="DOUBLE")
    window.set_title("[210 bold]Scripts").center()
    return window

def openWindow(fields: list) -> None:
    yamlConfig: str = loadStyleConfig("./yaml/config.yaml")

    with YamlLoader() as loader:
        loader.load(yamlConfig)

    with WindowManager() as manager:
        # name = InputField("Balazs", prompt="Name: ")
        # street = InputField("Some street", prompt="Address: ")
        # number = InputField("+11 0 123 456", prompt="Phone number: ")
        # additionalNotes = Container(
        #     "Additional notes:",
        #     InputField(
        #         "Some notes\nnew line note\nyada yada", multiline=True
        #     ),
        #     box="EMPTY_VERTICAL",
        # )
        # window = (
        #     Window(
        #         "",
        #         name,
        #         street,
        #         number,
        #         "",
        #         additionalNotes,
        #         "",
        #         ["Submit", lambda *_: submit(name.value, street.value, number.value)],
        #         width=60,
        #         box="DOUBLE",
        #     )
        #     .set_title("[210 bold]New contact").center()
        # )
        window = loadFields(fields)
        manager.add(window)
