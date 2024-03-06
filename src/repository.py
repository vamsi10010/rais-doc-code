import github
from tqdm import tqdm
from typing import List

# import src.constants if it exists
try:
    from src.constants import GITHUB_API_KEY
except:
    GITHUB_API_KEY = None
from src.block import BlockCollection, CodeBlock

class Repository:
    """
    A class to represent a repository to extract code blocks from.
    """
    
    def __init__(self, repo: str) -> None:
        self.repo: str = repo
        self.collections: List[BlockCollection] = []
        
            
    def build_collections(self, path: str = "") -> None:
        """Builds the collections of code blocks from the repository.
        
        Args:
            path (str, optional): The path to the directory to start from. Defaults to "".
        """
        
        if self.repo is None:
            raise ValueError("Repository not set.")
        if GITHUB_API_KEY is None:
            raise ValueError("GITHUB_API_KEY not set.")
        
        g = github.Github(GITHUB_API_KEY)
        repo = g.get_repo(self.repo)
        
        pbar = tqdm(total=0)
        
        self._traverse_dir(repo, pbar, path)
        
        print(f"Built successfully.\nTraversed {pbar.total} files. Found {len(self.collections)} collections.")
    
        
    
    def _traverse_dir(self,
                      repo: github.Repository.Repository,
                      pbar: tqdm, 
                      path: str = "") -> None:
        """Traverse a directory and find markdown files. If found, build a collection.

        Args:
            repo (github.Repository.Repository): Repository object.
            pbar (tqdm): Progess bar.
            path (str, optional): Directory path. Defaults to "".
        """
        
        contents = repo.get_contents(path)
        pbar.total += len(contents)
        for content in contents:
            if content.type == "dir":
                self._traverse_dir(repo, pbar, content.path)
                pbar.update(1)
            else:
                pbar.set_postfix(file=content.path)
                
                # if the file is a markdown file, build a collection
                if content.path.endswith(".md"):
                    md = content.decoded_content.decode()
                    collection = BlockCollection(title=content.path)
                    collection.add_to_collection(md)
                    self.collections.append(collection)
                    
                pbar.update(1)
            
     