from typing import List
from pathlib import Path

class Parser:
    extensions = List[str]

    def valid_extension(self, extension):
        for ext in self.extensions:
            if ext == extension:
                return True

        return False

    def parse(self, path, source, dest):
        raise NotImplementedError

    def read(self, path):
        with open(path) as file:
            return file.read()

    def write(self, path, dest, content, ext=".html"):
        full_path = self.dest / path.with_suffix().name(ext)
