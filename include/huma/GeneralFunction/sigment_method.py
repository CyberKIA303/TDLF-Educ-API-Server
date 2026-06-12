from .size_of import strsize

def esm(characters: str, invert: bool):
    return ESM_Sigment(characters, invert)

def osm(characters: str, invert: bool):
    return OSM_Sigment(characters, invert)

def ESM_Sigment(characters: str, invert: bool = False):
    output: str = ""
    size: int = strsize(characters)
    ems_n_sigment: int = 10
    ssf: bool = False
    if 1 == 1:
        I: int = 0
        while I < 4:
            if size % ems_n_sigment == 0:
                ssf = True
                break
            ems_n_sigment -= 2
            I += 1
    if not ssf:
        ems_n_sigment = 2
    if size % 2 == 0:
        sigment_size: int = size / ems_n_sigment
        s: list = {"0": "", "1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": ""}
        index: int = 0
        pss: int = 0
        for let in characters:
            s[f'{index}'] += let
            pss += 1
            if pss == sigment_size:
                index += 1
                pss = 0
        if sigment_size > 1:
            if 1 == 1:
                I: int = 0
                while I < ems_n_sigment:
                    s[f'{str(I)}'] = esm(s[f'{str(I)}'], invert)
                    I += 1
        if not invert:
            sc: int = int(ems_n_sigment)
            if sc == 10:
                output = s['5'] + s['7'] + s['9'] + s['1'] + s['3'] + s['6'] + s['8'] + s['0'] + s['2'] + s['4']
            elif sc == 8:
                output = s['5'] + s['7'] + s['6'] + s['4'] + s['3'] + s['1'] + s['0'] + s['2']
            elif sc == 6:
                output = s['1'] + s['3'] + s['5'] + s['0'] + s['2'] + s['4']
            elif sc == 4:
                output = s['2'] + s['0'] + s['3'] + s['1']
            elif sc == 2:
                output = s['1'] + s['0']
        else:
            sc: int = int(ems_n_sigment)
            if sc == 10:
                output = s['7'] + s['3'] + s['8'] + s['4'] + s['9'] + s['0'] + s['5'] + s['1'] + s['6'] + s['2']
            elif sc == 8:
                output = s['6'] + s['5'] + s['7'] + s['4'] + s['3'] + s['0'] + s['2'] + s['1']
            elif sc == 6:
                output = s['3'] + s['0'] + s['4'] + s['1'] + s['5'] + s['2']
            elif sc == 4:
                output = s['1'] + s['3'] + s['0'] + s['2']
            elif sc == 2:
                output = s['1'] + s['0']
    else:
        output = osm(characters, invert)
    return output

def OSM_Sigment(characters: str, invert: bool = False):
    output: str = ""
    size: int = strsize(characters)
    oms_n_sigment: int = 9
    if size % 2 != 0:
        ssf: bool = False
        if 1 == 1:
            I: int = 0
            while I < 4:
                if oms_n_sigment == size:
                    ssf = True
                    break
                srz: int = (size - (size % oms_n_sigment)) / oms_n_sigment
                if srz >= oms_n_sigment:
                    extra: int = size % oms_n_sigment
                    if extra > 0:
                        mid: int = srz + extra
                        if mid % 2 == 0:
                            ssf = True
                            break
                oms_n_sigment -= 2
                I += 1
        if not ssf:
            oms_n_sigment = 3
        sigment_size: int = (size - (size % oms_n_sigment)) / oms_n_sigment
        half_of_size: int = (oms_n_sigment - 1) / 2
        extent: int = size % oms_n_sigment
        s: list = {"0": "", "1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": ""}
        index: int = 0
        pss: int = 0
        is_half: bool = False
        for let in characters:
            s[f'{index}'] += let
            pss += 1
            if pss == sigment_size:
                index += 1
                pss = 0
                if index == half_of_size:
                    is_half = True
                    sigment_size += extent
                    continue
                if is_half:
                    is_half = False
                    sigment_size -= extent
        if sigment_size > 1:
            if 1 == 1:
                I: int = 0
                while I < oms_n_sigment:
                    s[f'{str(I)}'] = osm(s[f'{str(I)}'], invert)
                    I += 1
        if not invert:
            sc: int = int(oms_n_sigment)
            if sc == 9:
                output = s['5'] + s['7'] + s['0'] + s['2'] + s['4'] + s['6'] + s['8'] + s['1'] + s['3']
            elif sc == 7:
                output = s['5'] + s['6'] + s['4'] + s['3'] + s['2'] + s['0'] + s['1']
            elif sc == 5:
                output = s['1'] + s['4'] + s['2'] + s['0'] + s['3']
            elif sc == 3:
                output = s['2'] + s['1'] + s['0']
        else:
            sc: int = int(oms_n_sigment)
            if sc == 9:
                output = s['2'] + s['7'] + s['3'] + s['8'] + s['4'] + s['0'] + s['5'] + s['1'] + s['6']
            elif sc == 7:
                output = s['5'] + s['6'] + s['4'] + s['3'] + s['2'] + s['0'] + s['1']
            elif sc == 5:
                output = s['3'] + s['0'] + s['2'] + s['4'] + s['1']
            elif sc == 3:
                output = s['2'] + s['1'] + s['0']
    else:
        output = esm(characters, invert)
    return output