from pathlib import Path
import os
import tinytag


class MetadataExtractor:
    def __init__(self, directory_path):
        self.directory = directory_path

    def get_metadata(self, file):
        file_path = Path(file)
        return {"name": file_path.name,
            "size": Path.stat(file_path).st_size,
            "created_at": Path.stat(file_path).st_birthtime}



