import paramiko
import os
import sys

# SSH bağlantısı için gerekli bilgiler
hostname = sys.argv[1]  # IP adresi komut satırından alınacak
username = sys.argv[2]  # SSH kullanıcı adı komut satırından alınacak
password = sys.argv[3]  # SSH şifresi komut satırından alınacak
port = 22

command = 'show authentication session'

# Dosya yolları, hostname eklenerek oluşturulacak
desktop_path = os.path.join(os.getcwd(), 'data', 'AUTH-SESSION')
old_authsession_file_path = os.path.join(desktop_path, 'old-auth-session.txt')
new_authsession_file_path = os.path.join(desktop_path, 'new-auth-session.txt')
different_file_path = os.path.join(desktop_path, 'auth-session-different.txt')

# SSH bağlantısı kurma ve komutu çalıştırma
def get_auth_session(hostname, port, username, password, command, file_path):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, port, username, password)
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode()
        with open(file_path, 'w') as file:
            file.write(output)
        print(f"Authentication Session {file_path} dosyasına yazıldı.")
    except Exception as e:
        print(f"Hata: {e}")
    finally:
        ssh.close()

# Dosyaları karşılaştırma
def compare_authsession_files(old_file, new_file, diff_file):
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

# Yeni Authentication Session tablosunu çekme ve dosyaya yazma
get_auth_session(hostname, port, username, password, command, new_authsession_file_path)

# Dosyaları karşılaştırma
compare_authsession_files(old_authsession_file_path, new_authsession_file_path, different_file_path)
