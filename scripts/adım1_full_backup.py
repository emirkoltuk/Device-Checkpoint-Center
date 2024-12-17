import paramiko
import sys
import os

# SSH bağlantısı için gerekli bilgiler
hostname = sys.argv[1]  # IP adresi komut satırından alınacak
username = sys.argv[2]  # SSH kullanıcı adı komut satırından alınacak
password = sys.argv[3]  # SSH şifresi komut satırından alınacak
port = 22

# Full backup komutu
command = 'show running-config view full'

# Dosya yolu (yeni dosya yolu dizin yapısına göre güncellendi)
file_path = os.path.join(os.getcwd(), 'data', 'FULL_BACKUP', 'full_backup_different.txt')

# SSH bağlantısı kurma ve komutu çalıştırma
def get_full_backup(hostname, port, username, password, command, file_path):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, port, username, password)
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode()
        
        # Veriyi dosyaya yazma
        with open(file_path, 'w') as file:
            file.write(output)
        print(f"Tam yedek {file_path} dosyasına yazıldı.")
    except Exception as e:
        print(f"Hata: {e}")
    finally:
        ssh.close()

# Fonksiyonu çağırarak tam yedek alma ve dosyaya yazma
get_full_backup(hostname, port, username, password, command, file_path)