# Device Checkpoint Center

**Device Checkpoint Center**, ağ cihazlarından veri toplama, yedekleme ve karşılaştırma işlemlerini otomatikleştiren bir Python GUI uygulamasıdır. Bu proje, network mühendislerinin cihaz verilerini analiz ederek değişiklikleri tespit etmesini kolaylaştırır.

---

<p align="center">
  <img src="https://github.com/user-attachments/assets/d7d19576-bdb2-4da0-9c55-e532f5298d9f" alt="Figure 1" width="57%">
</p>

## 🔧 Projenin Amacı
Bu uygulama; VLAN, MAC Table, Interface Status, Access List, Full Backup ve Authentication Session gibi verileri ağ cihazlarından alıp, zaman içinde değişen durumları karşılaştırmalı olarak incelemenizi sağlar. 

**Ana Özellikler:**
- Python tabanlı otomatik veri toplama ve karşılaştırma.
- Kullanıcı dostu **Tkinter** arayüzü.
- Farklılıkları belirleyen detaylı raporlar.
- Modüler yapı sayesinde kolay genişletilebilir.

---

## 🛠 Kurulum
Bu projeyi kullanmak için aşağıdaki adımları takip edin:

### 1. Projeyi Klonlayın
```bash
git clone https://github.com/emirkoltuk/device-checkpoint-center.git
cd device-checkpoint-center
```

### 2. Gerekli Kütüphaneleri Yükleyin
```bash
pip install pillow, paramiko
```
> **Not**: Tkinter kütüphanesi Python'un standart kütüphaneleri arasında yer alır.

### 3. Uygulamayı Çalıştırın
Ana dosyayı çalıştırmak için aşağıdaki komutu kullanın:
```bash
python main.py
```

---

## 📅 Proje Dizin Yapısı
```
├── scripts/                  # Yedekleme ve karşılaştırma scriptleri
│   ├── adım1_mac.py          # Adım 1: MAC Table toplama
│   ├── adım1_full_backup.py  # Adım 1: Full Backup toplama
│   ├── adım1_vlan.py         # Adım 1: VLAN verisi toplama
│   ├── adım1_access.py       # Adım 1: Access List toplama
│   ├── adım1_interface-status.py  # Adım 1: Interface Status toplama
│   ├── adım1_auth-session.py # Adım 1: Auth Session toplama
│   ├── adım2_auth-session.py # Adım 2: Auth Session karşılaştırma
│   ├── adım2_interface-status.py  # Adım 2: Interface karşılaştırma
│   ├── adım2_mac.py          # Adım 2: MAC Table karşılaştırma
│   ├── adım2_vlan.py         # Adım 2: VLAN karşılaştırma
│   └── adım2_access.py       # Adım 2: Access List karşılaştırma
│
├── data/                     # Karşılaştırma sonuçları
│   ├── FULL_BACKUP/          # Full Backup farkları
│   ├── MAC_TABLE/            # MAC Table farkları
│   ├── VLAN/                 # VLAN farkları
│   ├── ACCESS_LIST/          # Access List farkları
│   ├── INTERFACE_STATUS/     # Interface Status farkları
│   └── AUTH-SESSION/         # Auth Session farkları
│
├── image.png                 # Ana ekran için logo
├── icon.png                  # Uygulama simgesi
└── main.py                   # Ana Uygulama
```

---

## 🔄 Kullanım

### 1. Ana Arayüz
Uygulamayı çalıştırdığınızda aşağıdaki seçenekler sunulacaktır:
- **Adım 1:** Ağ cihazlarından veri toplama (yedekleme).
- **Adım 2:** Toplanan verileri karşılaştırma.

### 2. Yedekleme İşlemi
- **"Adım 1"** sekmesini kullanarak gerekli veriyi toplamak için ilgili script çalıştırılır.
- Veriler, `data/` klasörü altına kaydedilir.

### 3. Karşılaştırma İşlemi
- **"Adım 2"** sekmesinden karşılaştırma işlemlerini başlatabilirsiniz.
- Farklılıklar özel txt dosyaları içine kaydedilir ve uygulama üzerinde görüntülenir.

### 4. Sonuçları Görüntüleme
- Oluşturulan fark raporları `data/` klasöründeki ilgili alt dizinlerde saklanır.

---

## 🎓 Teknik Detaylar

### Kullanılan Teknolojiler
- **Python** (Tkinter, Pillow)
- Modüler Python scriptleri

### Gereksinimler
- Python 3.8+
- Ağ cihazlarına SSH/CLI erişimi

### Sistem Gereksinimleri
- İşletim Sistemi: Windows/Linux/MacOS
- Python: En az 3.8

---

## 🔒 Güvenlik
- Script dosyalarında **kullanıcı adı, şifre veya hassas bilgiler** kesinlikle hardcoded olarak bulunmamalıdır.
- Ağ cihazlarına bağlantı için çevresel değişkenler veya güvenli kimlik yönetim sistemleri kullanılabilir.

---

## 📈 Geliştirme
### Yapılacak İyileştirmeler
- CLI desteği eklenmesi.
- Toplanan verilerin SQL veritabanına kaydedilmesi.
- Daha detaylı raporlama arayüzü.

Katkıda bulunmak için aşağıdaki adımları takip edin:
```bash
git clone https://github.com/kullanici_adi/device-checkpoint-center.git
cd device-checkpoint-center
git checkout -b yeni-ozellik
git add .
git commit -m "Yeni özellik eklendi: ..."
git push origin yeni-ozellik
```
---

## İletişim
Proje ile ilgili sorularınız için benimle iletişime geçebilirsiniz:
- **Muhammet Emir Koltuk**  
- **E-posta:** koltuk20@itu.edu.tr

---
