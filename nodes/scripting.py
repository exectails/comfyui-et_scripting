from typing import Any


class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False


anyType = AnyType("*")


class ETPythonTextScript3Node:
    """
    A node that takes a number of arguments and a Python script to execute
    them with. Intended as a bruteforce method if no general purpose string
    utility nodes are available for a certain function.
    """

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "script": ("STRING", {"multiline": True, "tooltip": "A python script to execute. Gets access to arg0~2 and may return text via a result variable."}),
            },
            "optional": {
                "arg0": (anyType, {"forceInput": True, "tooltip": "An argument passed to the script. Value is None if not connected."}),
                "arg1": (anyType, {"forceInput": True, "tooltip": "An argument passed to the script. Value is None if not connected."}),
                "arg2": (anyType, {"forceInput": True, "tooltip": "An argument passed to the script. Value is None if not connected."}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)

    CATEGORY = "exectails"
    FUNCTION = "process"

    def process(self, script, arg0=None, arg1=None, arg2=None) -> tuple:

        localVars = {}
        result = exec(script, {"arg0": arg0, "arg1": arg1, "arg2": arg2}, localVars)

        result = None
        if "result" in localVars:
            result = str(localVars["result"])

        return (result,)

    def flatten(self, value: list) -> str:
        return " ".join([str(s) for s in value])
