from decode_lists import decode_list

a = ['genocide', 'war crimes', 'apartheid', 'massacre', 'nakba', 'displacement', 'humanitarian crisis', 'blockade', 'occupatiob', 'refugees', 'icc', 'bds']
b = ['freedom flotilla', 'resistance', 'liberation', 'free palestine', 'gaza', 'ceasefire', 'protest', 'unrwa']
c = """The ongoing international debate often centers on allegations of Genocide and War Crimes within the region. Human 
    rights organizations frequently document the history of the Nakba, citing the continuous Displacement of Refugees and the 
    resulting Humanitarian Crisis. Critics of the current policy point to the Blockade and Occupation, often labeling the system as 
    Apartheid and calling for intervention by the ICC.
    On the streets, a global Protest movement advocates for BDS measures while chanting for Freedom and a Free Palestine. These 
    activists emphasize the importance of Resistance and Liberation, particularly in the context of anti-Zionism. Meanwhile, urgent 
    calls for Ceasefires in Gaza continue to grow, alongside efforts to protect the essential aid provided by UNRWA."""

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
    if percentage >= 40:
        return "high"
    elif percentage >= 25:
        return " medium"
    else:
        return "none"

def manager(hostile_list_encoded, less_hostile_list_encoded, text):
    hostile_list = decode_list(hostile_list_encoded)
    less_hostile_list = decode_list(less_hostile_list_encoded)
    data = {}
    data['bds_percent'] = set_bds_percent(hostile_list, less_hostile_list, text)
    data['is_bds'] = threshold(data['bds_percent'])
    data['bds_threat_level'] = set_threat_level(data['bds_percent'])
    return data

