import mistune
from typing import List

from src.utils import get_node_text

class CodeBlock:
    """
    A class to represent a code block in a markdown file.
    """
    
    def __init__(self, lang: str, desc: str, code: str) -> None:
        self.lang: str = lang
        self.desc: str = desc
        self.code: str = code
        self.type: str = None
        
    def set_type(self, type: str) -> None:
        """Set the type of the code block.

        Args:
            type : str
                The type of the code block.
        """
        
        self.type = type
        
    def __str__(self) -> str:
        return f"CodeBlock(\n\tLanguage: {self.lang}\n\tDescription: {self.desc}\n\tCode:\n{self.code})"
        
        
class BlockCollection:
    """
    A class to represent a collection of code blocks in a markdown file.
    """
    
    def __init__(self, title=None) -> None:
        self.blocks: List[CodeBlock] = []
        self.title: str = title
        
    
    def add_to_collection(self, md: str) -> None:
        """Find code blocks in a markdown file and populates self.blocks.

        Args:
            md : str
                The markdown file as a string.
        """
        
        if self.blocks is None:
            self.blocks = []
        
        markdown = mistune.create_markdown(renderer=mistune.AstRenderer())
        ast = markdown(md)
        
        desc = ""
        
        for node in ast:
            if node['type'] == 'block_code':
                lang = node['info']
                code = node['text']
                self.blocks.append(CodeBlock(lang, desc, code))
                desc = ""
            else:
                desc = get_node_text(node)
            
            
    def __str__(self) -> str:
        str = f"BlockCollection ---------------------------------\nTitle: {self.title}\nBlocks:\n"
        for block in self.blocks:
            str += f"{block}\n"
        str += "-------------------------------------------------"    
        
        return str