def extract_fields(data: dict):
    path = data["metadata"]["file_path"]
    ctime = data["metadata"]["created_at"]
    size = data["metadata"]['size']
    metadata = data["metadata"]
    return path, ctime, size, metadata

def set_mapping():
    mappings = {
        "properties": {
            "name": {"type": "text"},
            "size": {"type": "integer"},
            "created_at": {"type": "date"}
        }
    }
    return mappings