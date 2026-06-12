from datetime import datetime
from ..GeneralFunction import Length
from ..GeneralFunction import CBTN
from ..GeneralFunction import CNTB
from ..GeneralFunction import Charto

bibit = [
    {"valnum": 0, "bit64": "-"},
    {"valnum": 1, "bit64": "A"},
    {"valnum": 2, "bit64": "B"},
    {"valnum": 3, "bit64": "C"},
    {"valnum": 4, "bit64": "D"},
    {"valnum": 5, "bit64": "E"},
    {"valnum": 6, "bit64": "F"},
    {"valnum": 7, "bit64": "G"},
    {"valnum": 8, "bit64": "H"},
    {"valnum": 9, "bit64": "I"},
    {"valnum": 10,"bit64": "J"},
    {"valnum": 11,"bit64": "K"},
    {"valnum": 12,"bit64": "L"},
    {"valnum": 13,"bit64": "M"},
    {"valnum": 14,"bit64": "N"},
    {"valnum": 15,"bit64": "O"},
    {"valnum": 16,"bit64": "P"},
    {"valnum": 17,"bit64": "Q"},
    {"valnum": 18,"bit64": "R"},
    {"valnum": 19,"bit64": "S"},
    {"valnum": 20,"bit64": "T"},
    {"valnum": 21,"bit64": "U"},
    {"valnum": 22,"bit64": "V"},
    {"valnum": 23,"bit64": "W"},
    {"valnum": 24,"bit64": "X"},
    {"valnum": 25,"bit64": "Y"},
    {"valnum": 26,"bit64": "Z"},
    {"valnum": 27,"bit64": "a"},
    {"valnum": 28,"bit64": "b"},
    {"valnum": 29,"bit64": "c"},
    {"valnum": 30,"bit64": "d"},
    {"valnum": 31,"bit64": "e"},
    {"valnum": 32,"bit64": "f"},
    {"valnum": 33,"bit64": "g"},
    {"valnum": 34,"bit64": "h"},
    {"valnum": 35,"bit64": "i"},
    {"valnum": 36,"bit64": "j"},
    {"valnum": 37,"bit64": "k"},
    {"valnum": 38,"bit64": "l"},
    {"valnum": 39,"bit64": "m"},
    {"valnum": 40,"bit64": "n"},
    {"valnum": 41,"bit64": "o"},
    {"valnum": 42,"bit64": "p"},
    {"valnum": 43,"bit64": "q"},
    {"valnum": 44,"bit64": "r"},
    {"valnum": 45,"bit64": "s"},
    {"valnum": 46,"bit64": "t"},
    {"valnum": 47,"bit64": "u"},
    {"valnum": 48,"bit64": "v"},
    {"valnum": 49,"bit64": "w"},
    {"valnum": 50,"bit64": "x"},
    {"valnum": 51,"bit64": "y"},
    {"valnum": 52,"bit64": "z"},
    {"valnum": 53,"bit64": "0"},
    {"valnum": 54,"bit64": "1"},
    {"valnum": 55,"bit64": "2"},
    {"valnum": 56,"bit64": "3"},
    {"valnum": 57,"bit64": "4"},
    {"valnum": 58,"bit64": "5"},
    {"valnum": 59,"bit64": "6"},
    {"valnum": 60,"bit64": "7"},
    {"valnum": 61,"bit64": "8"},
    {"valnum": 62,"bit64": "9"},
    {"valnum": 63,"bit64": ":"},
    {"valnum": 64,"bit64": "="},
]

def binary_to_modified_bit64(binary: str):
    output = ""
    size = Length(binary)
    extent = 6 - (size % 6)
    val = ""
    valsize = 0
    end = "C"
    if extent != 6:
        end = str(extent)
    for let in binary:
        val += let
        valsize += 1
        if valsize == 6:
            bitval = CBTN(val)
            for b in bibit:
                if bitval == b['valnum']:
                    output += b['bit64']
                    break
            val = ""
            valsize = 0
    if valsize != 0:
        additivezero = ""
        while extent > 0:
            additivezero += "0"
            extent -= 1
        val = additivezero + val
        bitval = CBTN(val)
        for b in bibit:
            if bitval == b['valnum']:
                output += b['bit64']
                break
    datetimenow = datetime.now()
    start = Charto(Charto(str(datetimenow), " ", "-"), ".", ":")
    numberstring = start[21] + start[22]
    rand = (int(numberstring) % 10) + 1
    startsize = Length(start)
    index = rand
    trimstart = ""
    while index < startsize:
        trimstart += start[index]
        index += 1
    start = trimstart + "E"
    output = start + output + end
    return output

def modefied_bit64_to_binary(characters: str):
    output = ""
    size = Length(characters) - 1
    index = 0
    realdata = False
    while index < size:
        let = "" + characters[index]
        if realdata:
            val = 0
            for data in bibit:
                if let == data['bit64']:
                    val = data['valnum']
                    break
            binary = CNTB(val)
            if size - 1 == index and characters[-1] != 'C':
                trim = ""
                trimstart = int(characters[-1])
                for trm in binary:
                    if trimstart == 0:
                        trim += trm
                    else:
                        trimstart -= 1
                binary = trim
            output += binary
        elif let == "E" and not realdata:
            realdata = True
        index += 1
    return output