def extract_fields(data: dict):
    path = data["file_path"]
    ctime = data["metadata"]["created_at"]
    size = data["metadata"]['size']
    metadata = data["metadata"]
    return path, ctime, size, metadata

def set_mapping():
    mappings = {
        "properties": {
            "name": {"type": "text"},
            "size": {"type": "integer"},
            "created_at": {
                "type": "date",
                "format": "yyyy-MM-dd HH:mm:ss.SSSSSS"
                }
        }
    }
    return mappings