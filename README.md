ComfyUI - Scripting
=============================================================================

Collection of custom nodes for ComfyUI that can be used to write Python
scripts directly on a node. Useful for quick prototyping and testing,
though it comes at the cost of security, as custom scripts can do just
about anything.

**Do not use the custom nodes in this repository unless you know you can
trust the source of the workflow.**

Nodes
-----------------------------------------------------------------------------

### Python Text Script

A node that takes a number of arguments and passes them to a Python script.
After running the code, the node will output the value of the `result`
variable that you can set in the script.
