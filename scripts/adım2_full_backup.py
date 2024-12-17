import paramiko
import os
import sys

# SSH bağlantısı için gerekli bilgiler
hostname = sys.argv[1]  # IP adresi komut satırından alınacak
username = sys.argv[2]  # SSH kullanıcı adı komut satırından alınacak
password = sys.argv[3]  # SSH şifresi komut satırından alınacak
port = 22

# Full backup tablosunu çekmek için kullanılacak komut
command = 'show running-config view full'

# Dosya yolları
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # project-root dizin yolu
data_path = os.path.join(project_root, 'data', 'FULL_BACKUP')
old_full_backup_file_path = os.path.join(data_path, 'old_full_backup.txt')
new_full_backup_file_path = os.path.join(data_path, 'new_full_backup.txt')
different_file_path = os.path.join(data_path, 'full_backup_different.txt')

# SSH bağlantısı kurma ve komutu çalıştırma
def get_full_backup(hostname, port, username, password, command, file_path):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, port, username, password)
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode()
        with open(file_path, 'w') as file:
            file.write(output)
        print(f"Full Backup {file_path} dosyasına yazıldı.")
    except Exception as e:
        print(f"Hata: {e}")
    finally:
        ssh.close()

# Dosyaları karşılaştırma
def compare_backup_files(old_file, new_file, diff_file):
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

# Eski yedek dosyasının var olup olmadığını kontrol etme
if os.path.exists(old_full_backup_file_path):
    print("Eski yedek dosyası bulundu, yeni yedek alınacak ve farklar karşılaştırılacak.")
    # Yeni Full Backup dosyasını çekme ve dosyaya yazma
    get_full_backup(hostname, port, username, password, command, new_full_backup_file_path)
    
    # Dosyaları karşılaştırma
    compare_backup_files(old_full_backup_file_path, new_full_backup_file_path, different_file_path)
else:
    print(f"Eski yedek dosyası bulunamadı: {old_full_backup_file_path}. Yeni yedek alınacak.")
    # Yeni Full Backup dosyasını çekme ve dosyaya yazma
    get_full_backup(hostname, port, username, password, command, new_full_backup_file_path)
    print(f"Yeni yedek {new_full_backup_file_path} dosyasına kaydedildi.")
