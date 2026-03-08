from base64 import b64decode


hostile_list = "R2Vub2NpZGUvV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUvT2NjdXBhdGlvYixSZWZ1Z2VlcyxJQ0MsQkRT"
least_hostile_list = "RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ=="

def encode_list(lst): 
    lst = lst.strip().replace("=", "")
    remainder = len(lst) % 4
    print(len(lst))
    if 0 < remainder < 2:
        return False
    if remainder:
        lst += "=" * (4 - remainder)
    print(lst)
    result = b64decode(lst).decode()
    result = result.replace("/", ",").lower()
    return result.split(",")

print(encode_list(hostile_list))