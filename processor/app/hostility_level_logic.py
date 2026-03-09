from decode_lists import decode_list


def set_bds_percent(hostile_list, less_hostile_list, text):
    hostile = 2
    less_hostile = 1
    hostility_level = 0
    text = text.lower()
    text = text.split()
    for word in text:
        if word in hostile_list:
            hostility_level += hostile
            continue
        if word in less_hostile_list:
            hostility_level += less_hostile
    hostility_percent = 100 / len(text) * hostility_level
    return hostility_percent

def threshold(percentage):
    return percentage >= 40

def set_threat_level(percentage):
    if percentage >= 10:
        return "high"
    elif percentage >= 5:
        return " medium"
    else:
        return "none"

def manager(hostile_list_encoded, less_hostile_list_encoded, text):
    hostile_list = decode_list(hostile_list_encoded)
    less_hostile_list = decode_list(less_hostile_list_encoded)
    bds_percent = set_bds_percent(hostile_list, less_hostile_list, text)
    is_bds = threshold(bds_percent)
    bds_threat_level = set_threat_level(bds_percent)
    return bds_percent, is_bds, bds_threat_level

