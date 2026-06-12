import os
from fastapi.responses import FileResponse

path = os.path.join(os.path.dirname(__file__), 'Licences/')

def check_inque():
    with open(path + 'licence.access', 'r') as file:
        con = file.readline()
    if str(con) == "True":
        return True
    else:
        return False

def toggle_inque():
    data: bool = check_inque()
    with open(path + 'licence.access', 'w') as file:
        if data:
            file.write("False")
        else:
            file.write("True")

def update_file_content(data: str = "CONFIDENTIAL"):
    with open(path + 'tempural.licence', 'w') as file:
        file.write(data)
        
def get_licence_file():
    return FileResponse(path + "tempural.licence", media_type="application/octet-stream", filename="tempural.licence", headers={"Content-Disposition": "attachment; filename=project_licence.ddnhs_licence"})

def read_file_content(file_name: str):
    content: list = []
    with open(path + file_name, 'r') as file:
        con = file.readlines()
    for line in con:
        data = str(line)
        content.append({"data": data})
    return content