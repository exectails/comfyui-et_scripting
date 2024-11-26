from .nodes.scripting import ETPythonTextScript3Node

et_nodes = [
    ("Python Text Script (3 Arguments)", ETPythonTextScript3Node),
]

NODE_CLASS_MAPPINGS = {cls.__name__: cls for display_name, cls in et_nodes}
NODE_DISPLAY_NAME_MAPPINGS = {cls.__name__: display_name for display_name, cls in et_nodes}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
