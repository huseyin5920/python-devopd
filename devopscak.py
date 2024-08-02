from database.psql_connect import *

class Server():
    def __init__(self) -> None:
        self.server_name = ""
        self.server_ip = ""
        self.server_port = ""
        self.server_type = ""
        self.server_os_name = ""

    @classmethod
    def show_server_count(cls):
          print("5")

    @staticmethod
    def print_server_infos(server_name, server_ip, server_port, server_type, server_os_name):
            print(f"Server Name: {server_name}")
            print(f"Server IP: {server_ip}")
            print(f"Server Port: {server_port}")
            print(f"Server Type: {server_type}")
            print(f"Server OS Name: {server_os_name}")


server_instance = Server()
server_instance.server_name = "prod"
server_instance.server_ip = "192.168.1.4"
server_instance.server_port = "22"
server_instance.server_type = "on-prem"
server_instance.server_os_name = "Rocky Linux"


test = insert_server_info(
    server_instance.server_name,
    server_instance.server_ip,
    server_instance.server_port,
    server_instance.server_type,
    server_instance.server_os_name
)
print(test)
print("Server info inserted successfully")

Server().print_server_infos(server_instance.server_name, 
                            server_instance.server_ip, 
                            server_instance.server_port, 
                            server_instance.server_type, 
                            server_instance.server_os_name)
