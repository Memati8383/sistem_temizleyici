import os
import shutil
import ctypes
import sys
import platform
import subprocess
from pathlib import Path
import time

# Try to import tqdm, but don't fail if it's not available
try:
    from tqdm import tqdm
    HAS_TQDM = True
except ImportError:
    HAS_TQDM = False

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    """Restarts the current script with administrator privileges."""
    if is_admin():
        return True
    else:
        # Re-run the script with admin rights
        try:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            return False
        except:
            return False

def clean_system():
    if not is_admin():
        print("[!] HATA: Yönetici yetkisi alınamadı.")
        time.sleep(3)
        return

    print("="*50)
    print("        SİSTEM TEMİZLİK VE OPTİMİZASYON (PYTHON)")
    print("="*50)
    print()

    targets = [
        os.environ.get('TEMP'),
        r'C:\Windows\Temp',
        r'C:\Windows\Prefetch',
    ]
    
    # Recycle Bin
    recycle_bin = r'C:\$Recycle.bin'
    if os.path.exists(recycle_bin):
        targets.append(recycle_bin)

    print("[1/2] Dosyalar taranıyor ve boyut hesaplanıyor...")
    
    all_files = []
    total_bytes = 0
    
    for target in targets:
        if target and os.path.exists(target):
            for root, dirs, files in os.walk(target):
                for name in files:
                    file_path = os.path.join(root, name)
                    all_files.append(file_path)
                    try:
                        total_bytes += os.path.getsize(file_path)
                    except:
                        pass
                for name in dirs:
                    all_files.append(os.path.join(root, name))

    # Log files
    system_drive = os.environ.get('SystemDrive', 'C:')
    for p in Path(system_drive + '/').glob('*.log'):
        all_files.append(str(p))
        try:
            total_bytes += os.path.getsize(str(p))
        except:
            pass

    size_mb = round(total_bytes / (1024 * 1024), 2)
    print(f"Toplam silinecek veri: {size_mb} MB")
    print()

    if not all_files:
        print("[!] Silinecek dosya bulunamadı.")
    else:
        print("[2/2] Temizlik işlemi başlatılıyor...")
        
        if HAS_TQDM:
            with tqdm(total=len(all_files), unit="dosya", bar_format='{l_bar}{bar:30}{r_bar}{bar:-10b}') as pbar:
                for item in all_files:
                    try:
                        if os.path.isfile(item) or os.path.islink(item):
                            os.unlink(item)
                        elif os.path.isdir(item):
                            shutil.rmtree(item, ignore_errors=True)
                    except:
                        pass
                    pbar.update(1)
        else:
            for i, item in enumerate(all_files):
                try:
                    if os.path.isfile(item) or os.path.islink(item):
                        os.unlink(item)
                    elif os.path.isdir(item):
                        shutil.rmtree(item, ignore_errors=True)
                except:
                    pass
                if i % 10 == 0:
                    print(f"İşleniyor: {i}/{len(all_files)}", end='\r')

    print("\n\nDNS önbelleği temizleniyor...")
    try:
        subprocess.run(["ipconfig", "/flushdns"], capture_output=True, check=True)
    except:
        pass

    print("-" * 50)
    print(f"[✓] Temizlik başarıyla tamamlandı!")
    print(f"[i] Serbest bırakılan alan: ~{size_mb} MB")
    print()
    input("Kapatmak için Enter'a basın...")

if __name__ == "__main__":
    if platform.system() != "Windows":
        print("Bu araç sadece Windows işletim sisteminde çalışır.")
    else:
        if is_admin():
            clean_system()
        else:
            print("[i] Yönetici yetkisi isteniyor...")
            run_as_admin()
            sys.exit(0)  # Orijinal program kapanır, yeni yönetici penceresi açılır

