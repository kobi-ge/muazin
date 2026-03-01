from pathlib import Path

class Orchesrator:
    def __init__(self, logger, metadata_extractor):
        self.logger = logger
        self.metadata_extractor = metadata_extractor

    def run(self, directory_path):
        self.directory_path = Path(directory_path)
        for file_path in self.directory_path.iterdir():
            metadata = self.metadata_extractor.get_metadata(file_path)
            return {
                "metadata": metadata,
                "file_path": file_path
            }
        
