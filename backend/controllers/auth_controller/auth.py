import uuid
from backend.controllers.SQL_Controllers.execution import execute_query_on_connection
from backend.connection.SQL_Connection import nodes
from backend.security.password_handler import hash_password, verify_password
from backend.security.jwt_handler import create_access_token
import uuid

class Auth:
    @staticmethod
    def register(username, email, password):
        u_id = str(uuid.uuid4())
        query = """
        INSERT INTO user_info(user_info_id, username, user_email, user_password, user_status)
        VALUES (%s,%s,%s,%s,%s)
        RETURNING user_info_id, username
        """
        values = (
            u_id,
            username,
            email,
            hash_password(password),
            "active"
        )
        return execute_query_on_connection(
            nodes, query, values, True,
            [{"element_name":"user_id","element_row":0},
             {"element_name":"username","element_row":1}]
        )

    @staticmethod
    def login(email, password):
        query = """
        SELECT user_info_id, username, user_password
        FROM user_info WHERE user_email=%s
        """
        result = execute_query_on_connection(nodes, query, [email], True,
            [{"element_name":"user_id","element_row":0},
             {"element_name":"username","element_row":1},
             {"element_name":"password","element_row":2}])

        if not result:
            return None

        user=result[0]
        if not verify_password(password, user["password"]):
            return None

        token=create_access_token({
            "user_id": user["user_id"],
            "username": user["username"]
        })

        return {
            "access_token": token,
            "token_type":"bearer",
            "user_id": user["user_id"],
            "username": user["username"]
        }
