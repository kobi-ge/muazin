from pathlib import Path
from datetime import datetime


class MetadataExtractor:
    def __init__(self, logger):
        self.logger = logger

    def get_metadata(self, file_path):
        created_at = file_path.stat().st_birthtime
        created_at = datetime.fromtimestamp(created_at)
        return {"name": file_path.name,
            "size": file_path.stat().st_size,
            "created_at": created_at}
