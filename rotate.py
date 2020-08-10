def rotate_dict_values(dic , step):
    keys = list(dic.keys())
    values = list(dic.values())
    newValues = values.copy()

    for i in range(0 , len(values)):
        rot_step = abs(i+step) % len(values)
        if((i+step) >= 0):
            newValues[rot_step] = values[i]
        else:
            newValues[-rot_step] = values[i]

    return  dict(zip(keys,newValues))


def rotate_dict_keys(dic , step):
    keys = list(dic.keys())
    values = list(dic.values())
    newKeys = keys.copy()

    for i in range(0 , len(keys)):
        rot_step = abs(i+step) % len(keys)
        if((i+step) >= 0):
            newKeys[rot_step] = keys[i]
        else:
            newKeys[-rot_step] = keys[i]
                           
    return  dict(zip(newKeys,values))

def interchange_keys_values(dic):
    keys = list(dic.keys())
    values = list(dic.values())
    newKeys  = keys.copy()
    newValues = values.copy()

    for x in range (0 , len(keys)):
        newValues[x] = keys[x]
        newKeys[x] = values[x]

    return dict(zip(newKeys , newValues))
