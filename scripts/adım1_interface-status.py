import paramiko
import sys

hostname = sys.argv[1]  # IP adresi komut satırından alınacak
username = sys.argv[2]  # SSH kullanıcı adı komut satırından alınacak
password = sys.argv[3]  # SSH şifresi komut satırından alınacak
port = 22

command = 'show interface status'

file_path = './data/INTERFACE_STATUS/old-interface-status.txt'

def get_interface_status(hostname, port, username, password, command, file_path):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, port, username, password)
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode()
        with open(file_path, 'w') as file:
            file.write(output)
        print(f"Interface status {file_path} dosyasına yazıldı.")
    except Exception as e:
        print(f"Hata: {e}")
    finally:
        ssh.close()

get_interface_status(hostname, port, username, password, command, file_path)