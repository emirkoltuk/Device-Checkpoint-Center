import paramiko
import os
import sys

hostname = sys.argv[1]  # IP adresi komut satırından alınacak
username = sys.argv[2]  # SSH kullanıcı adı komut satırından alınacak
password = sys.argv[3]  # SSH şifresi komut satırından alınacak
port = 22

command = 'show vlan'

desktop_path = './data/VLAN/'
old_vlan_file_path = os.path.join(desktop_path, f'old-vlan.txt')
new_vlan_file_path = os.path.join(desktop_path, f'new-vlan.txt')
different_file_path = os.path.join(desktop_path, f'vlan-different.txt')

def get_vlan_table(hostname, port, username, password, command, file_path):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, port, username, password)
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode()
        with open(file_path, 'w') as file:
            file.write(output)
        print(f"VLAN tablosu {file_path} dosyasına yazıldı.")
    except Exception as e:
        print(f"Hata: {e}")
    finally:
        ssh.close()

def compare_vlan_files(old_file, new_file, diff_file):
    try:
        with open(old_file, 'r') as f1, open(new_file, 'r') as f2:
            old_lines = set(f1.readlines())
            new_lines = set(f2.readlines())
        differences = old_lines.symmetric_difference(new_lines)
        with open(diff_file, 'w') as f:
            f.writelines(differences)
        print(f"Farklılıklar {diff_file} dosyasına yazıldı.")
    except Exception as e:
        print(f"Hata: {e}")

get_vlan_table(hostname, port, username, password, command, new_vlan_file_path)

compare_vlan_files(old_vlan_file_path, new_vlan_file_path, different_file_path)