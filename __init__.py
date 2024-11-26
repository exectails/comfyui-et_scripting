from .nodes.scripting import ETPythonTextScript3Node

NODE_CLASS_MAPPINGS = {
    "ETPythonTextScript3Node": ETPythonTextScript3Node,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ETPythonTextScript3Node": "Python Text Script (3 Arguments)",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
