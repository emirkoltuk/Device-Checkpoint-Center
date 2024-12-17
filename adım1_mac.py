import paramiko
import sys

hostname = sys.argv[1]
username = sys.argv[2] 
password = sys.argv[3]
port = 22

command = 'show mac address-table'

file_path = '/opt/dcs/data/MAC_TABLE/old-mac.txt'

def get_mac_address_table(hostname, port, username, password, command, file_path):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, port, username, password)
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode()
        with open(file_path, 'w') as file:
            file.write(output)
        print(f"MAC address tablosu {file_path} dosyasına yazıldı.")
    except Exception as e:
        print(f"Hata: {e}")
    finally:
        ssh.close()

get_mac_address_table(hostname, port, username, password, command, file_path)
