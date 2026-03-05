import hashlib

def generate_unique_id(path, ctime, size):
    full_str = path + ctime + str(size)
    res = hashlib.md5(full_str.encode())
    return res.hexdigest()

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

def file_to_bytes(file_path):
    with open(file_path, "rb") as file:
        return file.read()