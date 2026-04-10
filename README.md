<div align="center">

# 🛡️ NIKO Sistem Temizleyici v3.0

**Windows · macOS · Linux**

Geçici dosyaları, önbellekleri ve sistem çöplerini temizleyen gelişmiş bir terminal aracı.

![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows%20|%20macOS%20|%20Linux-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</div>

---

## ✨ Özellikler

| Özellik | Açıklama |
|---------|----------|
| 🖥️ **Çapraz Platform** | Windows, macOS ve Linux otomatik algılama ve platforma özel temizlik |
| 🗑️ **Geçici Dosya Temizliği** | TEMP, sistem cache, prefetch ve önbellek dizinlerini temizler |
| ♻️ **Çöp Kutusu** | Geri dönüşüm kutusu / Trash boşaltma |
| 📋 **Log Temizliği** | Sistem log dosyalarını temizler |
| 🌐 **DNS Temizliği** | DNS önbelleğini temizleyerek bağlantıyı tazeler |
| 📊 **Animasyonlu Arayüz** | Renkli progress bar, loading animasyonları, ikonlar |
| 🔒 **Otomatik Yetki** | Windows'ta UAC, Linux/macOS'ta sudo yetki kontrolü |
| ⏱️ **Süre Ölçümü** | Toplam temizlik süresi raporlama |

## 🎨 Ekran Görüntüsü

```
    +============================================================+
    |                                                            |
    |   ##    ## #### ##    ##  #######                           |
    |   ## ## ##  ##  #####    ##     ##                          |
    |   ##    ## #### ##    ##  #######                           |
    |                                                            |
    |     Sistem Temizleyici v3.0  |  Windows * macOS * Linux    |
    |                                                            |
    +============================================================+

    +-- SISTEM BILGISI ------------------------------------------+
    |  [WIN]  Isletim Sistemi  :  Windows (10, Build 10.0.19045) |
    |  [PC ]  Makine           :  DESKTOP-ABC123                 |
    |  [CPU]  Mimari           :  AMD64                          |
    |  [PY ]  Python           :  3.11.9                         |
    +------------------------------------------------------------+

    ◆ [1] Hedef Dizinler Taraniyor
    .......................................................
        |-- C:\Users\USER\AppData\Local\Temp
        |-- C:\Windows\Temp
        |-- C:\Windows\Prefetch
        '-- C:\$Recycle.bin
     ▶ 4 hedef dizin tespit edildi.

    ◆ [3] Temizlik Islemi
    / Temizleniyor...   [████████████████████████████░░░░] 87.5%
```

## 📋 Gereksinimler

- **Python 3.7** veya üzeri
- Ek kütüphane gerektirmez (sadece standart kütüphane kullanılır)

## 🚀 Kurulum ve Kullanım

### Windows

```bash
# Doğrudan çalıştır (UAC otomatik olarak yetki isteyecek)
python main.py

# veya sağ tıklayıp "Yönetici olarak çalıştır"
```

### macOS

```bash
sudo python3 main.py
```

### Linux

```bash
sudo python3 main.py
```

## 🧹 Temizlenen Alanlar

### Windows
| Alan | Yol |
|------|-----|
| Kullanıcı geçici dosyalar | `%TEMP%` |
| Sistem geçici dosyalar | `C:\Windows\Temp` |
| Prefetch verileri | `C:\Windows\Prefetch` |
| Geri dönüşüm kutusu | `C:\$Recycle.bin` |
| Güncelleme önbelleği | `C:\Windows\SoftwareDistribution\Download` |
| Küçük resim önbelleği | `%LOCALAPPDATA%\Microsoft\Windows\Explorer` |
| Log dosyaları | `C:\*.log`, `C:\Windows\Logs\**\*.log` |

### macOS
| Alan | Yol |
|------|-----|
| Uygulama önbelleği | `~/Library/Caches` |
| Log dosyaları | `~/Library/Logs`, `/private/var/log` |
| Geçici dosyalar | `/private/tmp`, `/tmp` |
| Çöp kutusu | `~/.Trash` |
| Chrome önbelleği | `~/Library/Caches/Google/Chrome` |

### Linux
| Alan | Yol |
|------|-----|
| Kullanıcı önbelleği | `~/.cache` |
| Sistem geçici dosyalar | `/tmp`, `/var/tmp` |
| Log dosyaları | `/var/log` |
| Çöp kutusu | `~/.local/share/Trash` |
| Küçük resim önbelleği | `~/.cache/thumbnails` |

## 📦 EXE Oluşturma (Windows)

Tek dosya olarak dağıtmak için PyInstaller kullanabilirsiniz:

```bash
# PyInstaller yükle
pip install pyinstaller

# EXE oluştur (PATH sorunu yaşamamak için 'python -m' kullanın)
python -m PyInstaller --onefile --uac-admin --name="NikoTemizleyici" main.py
```

Oluşan dosya `dist/` klasöründe yer alacaktır.

## ⚠️ Notlar

- Kullanımda olan bazı dosyalar silinemeyebilir — bu normaldir ve program bunları atlayarak devam eder.
- Windows'ta **Yönetici**, macOS/Linux'ta **root** yetkisi gereklidir.
- Program hiçbir üçüncü parti kütüphane gerektirmez.
- Tüm renk ve animasyonlar standart ANSI escape kodları ile çalışır.

## 📁 Proje Yapısı

```
sistem_temizleyici/
├── main.py          # Ana program dosyası
└── README.md        # Bu dosya
```

## 📄 Lisans

Bu proje MIT lisansı ile lisanslanmıştır.

---

<div align="center">

**Niko Interactive** tarafından geliştirilmiştir.

</div>
