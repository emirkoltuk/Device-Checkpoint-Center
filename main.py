import tkinter as tk
from tkinter import ttk, Scrollbar, Canvas, messagebox
from tkinter import scrolledtext
from PIL import Image, ImageTk
import subprocess
import os

script_directory = './scripts/'
image_path = './assets/image.png'
icon_path = './assets/icon.png' 
backup_file_path = './data/FULL_BACKUP/full_backup_different.txt'
mac_diff_file_path = './data/MAC_TABLE/mac-different.txt'
vlan_diff_file_path = './data/VLAN/vlan-different.txt'
access_diff_file_path = './data/ACCESS_LIST/access-different.txt'
istatus_diff_file_path = './data/INTERFACE_STATUS/interface-status-different.txt'
backup_different_file_path = './data/FULL_BACKUP/full_backup_different.txt'
auth_session_different_file_path = './data/AUTH-SESSION/auth-session-different.txt'

def run_backup(ip_address, username, password):
    try:
        subprocess.run(['python', os.path.join(script_directory, 'adım1_mac.py'), ip_address, username, password], check=True)
        subprocess.run(['python', os.path.join(script_directory, 'adım1_full_backup.py'), ip_address, username, password], check=True)
        subprocess.run(['python', os.path.join(script_directory, 'adım1_vlan.py'), ip_address, username, password], check=True)
        subprocess.run(['python', os.path.join(script_directory, 'adım1_access.py'), ip_address, username, password], check=True)
        subprocess.run(['python', os.path.join(script_directory, 'adım1_interface-status.py'), ip_address, username, password], check=True)
        subprocess.run(['python', os.path.join(script_directory, 'adım1_auth-session.py'), ip_address, username, password], check=True)
        messagebox.showinfo("Info", "Backup Authentication Session, Interface Status, VLAN, MAC Table, and Access List data is completed.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Hata", f"Backup çalıştırılırken bir hata oluştu: {e}")

def run_step2_auth_session(ip_address, username, password):
    try:
        subprocess.run(['python', os.path.join(script_directory, 'adım2_auth-session.py'), ip_address, username, password], check=True)
        messagebox.showinfo("Info", "New device Auth-Session data is completed and compared with Backup.")
        show_file_content(auth_session_different_file_path, authsession_tab)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Hata", f"Adım2 çalıştırılırken bir hata oluştu: {e}")

def run_step2_istatus(ip_address, username, password):
    try:
        subprocess.run(['python', os.path.join(script_directory, 'adım2_interface-status.py'), ip_address, username, password], check=True)
        messagebox.showinfo("Info", "New device Interface Status data is completed and compared with Backup.")
        show_file_content(istatus_diff_file_path, istatus_tab)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Hata", f"Adım2 çalıştırılırken bir hata oluştu: {e}")

def run_step2_mac(ip_address, username, password):
    try:
        subprocess.run(['python', os.path.join(script_directory, 'adım2_mac.py'), ip_address, username, password], check=True)
        messagebox.showinfo("Info", "New device MAC Table data is completed and compared with Backup.")
        show_file_content(mac_diff_file_path, mac_tab)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Hata", f"Adım2 çalıştırılırken bir hata oluştu: {e}")

def run_step2_vlan(ip_address, username, password):
    try:
        subprocess.run(['python', os.path.join(script_directory, 'adım2_vlan.py'), ip_address, username, password], check=True)
        messagebox.showinfo("Info", "New device VLAN data is completed and compared with Backup.")
        show_file_content(vlan_diff_file_path, vlan_tab)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Hata", f"Yeni VLAN toplarken bir hata oluştu: {e}")

def run_step2_access(ip_address, username, password):
    try:
        subprocess.run(['python', os.path.join(script_directory, 'adım2_access.py'), ip_address, username, password], check=True)
        messagebox.showinfo("Info", "New device Access List data is completed and compared with Backup.")
        show_file_content(access_diff_file_path, access_tab)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Hata", f"Yeni Access List toplarken bir hata oluştu: {e}")

def run_full_backup(ip_address, username, password):
    try:
        subprocess.run(['python', os.path.join(script_directory, 'adım1_full_backup.py'), ip_address, username, password], check=True)
        messagebox.showinfo("Info", "Full backup işlemi tamamlandı.")
        show_file_content(backup_file_path, backup_tab)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Hata", f"Full backup alınırken bir hata oluştu: {e}")

def run_step2_full_backup(ip_address, username, password):
    try:
        subprocess.run(['python', os.path.join(script_directory, 'adım2_full_backup.py'), ip_address, username, password], check=True)
        messagebox.showinfo("Info", "Yeni FULL BACKUP işlemi tamamlandı ve Backup ile karşılaştırıldı.")
        show_file_content(backup_different_file_path, full_backup_diff_tab)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Hata", f"FULL BACKUP çalıştırılırken bir hata oluştu: {e}")

def show_file_content(file_path, tab):
    try:
        with open(file_path, 'r') as file:
            tab_content[tab].delete(1.0, tk.END)
            tab_content[tab].insert(tk.END, file.read())
        notebook.select(tab)
    except Exception as e:
        messagebox.showerror("Hata", f"Dosya okunurken bir hata oluştu: {e}")

def main():
    global notebook, tab_content, backup_tab, mac_tab, vlan_tab, access_tab, full_backup_diff_tab, istatus_tab, authsession_tab

    root = tk.Tk()
    root.title("Device Checkpoint Center")
    root.geometry("900x750")
    root.configure(bg="#f0f0f0")

    try:
        icon_image = Image.open(icon_path)
        icon_image = icon_image.resize((32, 32), Image.LANCZOS)
        icon_photo = ImageTk.PhotoImage(icon_image)
        root.iconphoto(True, icon_photo)
    except Exception as e:
        print(f"Icon loading error: {e}")

    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill='both')

    tab_content = {}

    main_frame = ttk.Frame(notebook, padding="10")
    notebook.add(main_frame, text='Main')

    title_label = tk.Label(main_frame, text="Device Checkpoint Center", font=("Arial", 17, "bold"))
    title_label.pack(pady=(19, 10))

    input_frame = ttk.Frame(main_frame, padding="10")
    input_frame.pack(pady=10, padx=20, fill="x")

    ttk.Label(input_frame, text="IP Address:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    ip_entry = ttk.Entry(input_frame, width=30)
    ip_entry.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(input_frame, text="Username:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    username_entry = ttk.Entry(input_frame, width=30)
    username_entry.grid(row=1, column=1, padx=5, pady=5)

    ttk.Label(input_frame, text="Password:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    password_entry = ttk.Entry(input_frame, show='*', width=30)
    password_entry.grid(row=2, column=1, padx=5, pady=5)

    button_frame = ttk.Frame(input_frame, padding="10")
    button_frame.grid(row=0, column=2, rowspan=3, padx=5, pady=5, sticky="ns")

    backup_button = ttk.Button(button_frame, text="TEST-BACKUP", command=lambda: run_backup(ip_entry.get(), username_entry.get(), password_entry.get()), width=20)
    backup_button.grid(row=1, column=0, pady=18, sticky="ew")

    test_frame = ttk.LabelFrame(main_frame, text="TEST", padding="10")
    test_frame.pack(pady=10)

    ttk.Button(test_frame, text="MAC-TABLE", command=lambda: run_step2_mac(ip_entry.get(), username_entry.get(), password_entry.get())).pack(pady=5, fill="x")
    ttk.Button(test_frame, text="AUTH-SESSION", command=lambda: run_step2_auth_session(ip_entry.get(), username_entry.get(), password_entry.get())).pack(pady=5, fill="x")
    ttk.Button(test_frame, text="INTERFACE-STATUS", command=lambda: run_step2_istatus(ip_entry.get(), username_entry.get(), password_entry.get())).pack(pady=5, fill="x")
    ttk.Button(test_frame, text="VLAN", command=lambda: run_step2_vlan(ip_entry.get(), username_entry.get(), password_entry.get())).pack(pady=5, fill="x")
    ttk.Button(test_frame, text="ACCESS-LIST", command=lambda: run_step2_access(ip_entry.get(), username_entry.get(), password_entry.get())).pack(pady=5, fill="x")
    ttk.Button(test_frame, text="BACKUP", command=lambda: run_step2_full_backup(ip_entry.get(), username_entry.get(), password_entry.get())).pack(pady=5, fill="x")

    info_label = ttk.Label(main_frame, text="When the operations are complete, you will be notified.", font=("Arial", 12))
    info_label.pack(pady=10)

    backup_tab = ttk.Frame(notebook, padding="10")
    notebook.add(backup_tab, text='Full Backup')

    tab_content[backup_tab] = scrolledtext.ScrolledText(backup_tab, wrap=tk.WORD)
    tab_content[backup_tab].pack(expand=True, fill='both')

    authsession_tab = ttk.Frame(notebook, padding="10")
    notebook.add(authsession_tab, text='Auth-Session')

    tab_content[authsession_tab] = scrolledtext.ScrolledText(authsession_tab, wrap=tk.WORD)
    tab_content[authsession_tab].pack(expand=True, fill='both')

    mac_tab = ttk.Frame(notebook, padding="10")
    notebook.add(mac_tab, text='MAC-TABLE')

    tab_content[mac_tab] = scrolledtext.ScrolledText(mac_tab, wrap=tk.WORD)
    tab_content[mac_tab].pack(expand=True, fill='both')

    vlan_tab = ttk.Frame(notebook, padding="10")
    notebook.add(vlan_tab, text='VLAN')

    tab_content[vlan_tab] = scrolledtext.ScrolledText(vlan_tab, wrap=tk.WORD)
    tab_content[vlan_tab].pack(expand=True, fill='both')

    access_tab = ttk.Frame(notebook, padding="10")
    notebook.add(access_tab, text='ACCESS-LIST')

    tab_content[access_tab] = scrolledtext.ScrolledText(access_tab, wrap=tk.WORD)
    tab_content[access_tab].pack(expand=True, fill='both')

    full_backup_diff_tab = ttk.Frame(notebook, padding="10")
    notebook.add(full_backup_diff_tab, text='Full Backup Diff.')

    tab_content[full_backup_diff_tab] = scrolledtext.ScrolledText(full_backup_diff_tab, wrap=tk.WORD)
    tab_content[full_backup_diff_tab].pack(expand=True, fill='both')

    istatus_tab = ttk.Frame(notebook, padding="10")
    notebook.add(istatus_tab, text='Interface Status')

    tab_content[istatus_tab] = scrolledtext.ScrolledText(istatus_tab, wrap=tk.WORD)
    tab_content[istatus_tab].pack(expand=True, fill='both')  

    root.mainloop()

if __name__ == "__main__":
    main()