from typing import Dict

def get_node_text(node: Dict) -> str:
    """Extract all text from a markdown node and its children recursively.

    Args:
        node (dict): Markdown Node

    Returns:
        str: Text
    """
    text = node.get('text', '')
    children = node.get('children', [])
    for child in children:
        text += get_node_text(child)
        
    return text