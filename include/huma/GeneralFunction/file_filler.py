def default():
    return [{"target": "None", "data": None, "len_type": "word", "remove_col": False}]

def fill_file_content(file_data: list, filler: list = default()):
    output: list = []
    line_data: str = ""
    target: str = ""
    on_target: bool = False
    for line in file_data:
        line_data = ""
        in_line: str = line['data']
        for let in in_line:
            if let == '"' and not on_target:
                on_target = True
                continue
            elif let == '"':
                on_target = False
                found: bool = False
                for com in filler:
                    if com['target'] == target:
                        if com['len_type'] == "word":
                            if com['remove_col']:
                                line_data += str(com['data'])
                            else:
                                line_data += str('"' + com['data'] + '"')
                        else:
                            is_first: bool = True
                            multi_data: list = com['data']
                            for ins in multi_data:
                                if ins['last']:
                                    line_data = ins['data']
                                    break
                                if is_first:
                                    if not com['remove_col']:
                                        line_data += str('"')
                                    line_data += str(ins['data'])
                                    output.append({"data": str(line_data + "\n")})
                                    is_first = False
                                else:
                                    output.append({"data": str(ins['data'] + "\n")})
                            if not com['remove_col']:
                                line_data += str('"')
                        found = True
                        break
                if not found:
                    line_data += str('"' + target + '"')
                target = ""
                continue
            if on_target:
                target += let
            else:
                line_data += let
        output.append({"data": line_data})
    return output