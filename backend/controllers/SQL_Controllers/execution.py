import os
import sys
import psycopg2
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def execute_query_on_connection(nodes: list, query: str, values: list = None, value_return: bool = False, returned_element: list = [{"element_name": "NULL", "element_row": 0}], target_data_base: str = "!!!"):
    returned_output: list = []
    for node in nodes:
        if target_data_base != "!!!":
            if node['database'] != target_data_base:
                continue
        try:
            conn = psycopg2.connect(
                host = node["host"],
                port = node["port"],
                dbname = node["database"],
                user = node["user"],
                password = node["password"]
            )
            cur = conn.cursor()
            if values:
                cur.execute(query, values)
            else:
                cur.execute(query)
            if value_return:
                rows = cur.fetchall()
                trim: list = []
                for row in rows:
                    fin = {str(item['element_name']): row[int(item['element_row'])] for item in returned_element}
                    add = fin
                    trim.append(add)
                setnip = trim
                returned_output.append({"database": node['database'], "data": setnip})
            else:
                conn.commit()
            cur.close()
            conn.close()
            if value_return:
                return returned_output
            else:
                return "QUERY SUCCESSFUL."
        except Exception as e:
            error = f"Error on {node['type']}: {e}"
            return error