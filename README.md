ComfyUI - Scripting
=============================================================================

Collection of custom nodes for ComfyUI that can be used to write Python
scripts directly on a node. Useful for quick prototyping and testing,
though it comes at the cost of security, as custom scripts can do just
about anything.

**Do not use the custom nodes in this repository unless you know you can
trust the source of the workflow.**

Install
-----------------------------------------------------------------------------

Clone the repository into your ComfyUI custom_nodes directory.
```text
git clone https://github.com/exectails/comfyui-et_scripting
```

Nodes
-----------------------------------------------------------------------------

### Python Text Script

A node that takes a number of inputs as well as a Python script that
takes the given arguments to produce a result. Intended as a brute-
force method in cases where a general purpose formatter might not
cut it and no dedicated node is available. The value assigned to
the `result` variable inside the script will be returned by the
node.

**Example**

Return a description based on a numeric input.

Script
```python
age = int(arg0)

if age < 13:
    result = "a nice child"
elif age < 22:
    result = "an angsty teen"
else:
    result = "a mature adult"
```

Input
```text
arg0: 17
```

Onput
```text
"an angsty teenager"
```
