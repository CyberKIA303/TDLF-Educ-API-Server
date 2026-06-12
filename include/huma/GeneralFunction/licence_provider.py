import os
from . import WSM
from .size_of import strsize
from datetime import datetime
from ..CyperFunction import Charbi
from ..LicenceFolder import check_inque
from ..LicenceFolder import toggle_inque
from .file_filler import fill_file_content
from fastapi.responses import FileResponse
from ..LicenceFolder import get_licence_file
from ..LicenceFolder import read_file_content
from ..LicenceFolder import update_file_content
from .datetime_extention import add_5years_terms
from .datetime_extention import simplify_datetime
from .datetime_extention import get_modern_datetime_now

def data_to_be_inserted(User_Name: str, Project_Name: str, Project_Version: str, Date_Now: str, Term_End: str):
    obstruct_data = [
        {"target": "User Name", "data": User_Name, "len_type": "word", "remove_col": False},
        {"target": "Project Name", "data": Project_Name, "len_type": "word", "remove_col": False},
        {"target": "Project Version", "data": Project_Version, "len_type": "word", "remove_col": False},
        {"target": "Date and Time Issued", "data": Date_Now, "len_type": "word", "remove_col": False},
        {"target": "Date and Time End of Term", "data": Term_End, "len_type": "word", "remove_col": False},
    ]
    return obstruct_data

def add_binary_data(data: list):
    obstruct_data = [
        {"target": "Random 1 and 0", "data": data, "len_type": "line", "remove_col": True},
    ]
    return obstruct_data

def purify_data(data: str):
    output: str = ""
    for let in data:
        if let != ' ':
            output += let
    return output

def get_ddnhs_project_licence(User_Name: str, Project_Name: str, Project_Version: str):
    check_if_free: bool = check_inque()
    if check_if_free:
        toggle_inque()
        now: datetime = datetime
        licence_content: list = read_file_content("project_licence.ddnhs_licence.example")
        date_now: str = get_modern_datetime_now(now)
        term_end: str = get_modern_datetime_now(now, 5)
        licence: list = fill_file_content(licence_content, data_to_be_inserted(User_Name, Project_Name, Project_Version, date_now, term_end))
        hash_overal_license: str = str(licence[4]['data'] + licence[5]['data'] + licence[9]['data'] + licence[10]['data'])
        hash_overal_license = str(" " + Charbi(WSM(hash_overal_license)) + " ")
        binary_license: list = []
        limit: int = 0
        if strsize(licence[4]['data']) > strsize(licence[5]['data']):
            limit = strsize(licence[4]['data'])
        else:
            limit = strsize(licence[5]['data'])
        license_size_data: int = strsize(hash_overal_license)
        index: int = 0
        cut_data: str = ""
        temp_index: int = 0
        while index < license_size_data:
            if temp_index == limit - 1:
                if license_size_data - 1 - index == 0:
                    binary_license.append({"data": cut_data, "last": True})
                else:
                    binary_license.append({"data": cut_data, "last": False})
                cut_data = ""
                temp_index = 0
            cut_data += hash_overal_license[index]
            temp_index += 1
            index += 1
        if cut_data != "":
            binary_license.append({"data": cut_data, "last": True})
        for contex in binary_license:
            gtx: str = contex['data']
            if gtx[0] == ' ':
                gtx = str(" " + WSM(purify_data(gtx)))
            elif gtx[-1] == ' ':
                gtx = str(WSM(purify_data(gtx)) + " ")
            else:
                gtx = WSM(gtx)
            contex['data'] = gtx
        licence_content = licence
        licence = fill_file_content(licence_content, add_binary_data(binary_license))
        content: str = ""
        for data in licence:
            content += data['data']
        update_file_content(content)
        toggle_inque()
        return get_licence_file()
    else:
        return "Server Bussy!"
    
def download_pdf():
    path = "C:/Users/dexte/Downloads/"
    files = [
        "PPT TEMPLATE FOR MSU TCTO.pptx",
        "546108343_778060441633760_1925230619270526032_n.png",
        "fastAPI-main.zip",
        "python-3.13.7-amd64.exe",
        "202204262121.mp4",
        "Vidio-scene-take.docx"
    ]
    file_name = files[5]
    return FileResponse(path + file_name, media_type="application/octet-stream", filename=file_name, headers={"Content-Disposition": "attachment; filename=" + file_name})