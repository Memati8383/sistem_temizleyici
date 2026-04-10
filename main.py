#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ============================================================================
#  NIKO SISTEM TEMIZLEYICI v3.0 - Windows / macOS / Linux
#  Gelistirici: Niko Interactive
# ============================================================================

import os, shutil, ctypes, sys, platform, subprocess, glob, time
from pathlib import Path
from datetime import datetime


# ============================================================================
#  KONSOL YAPILANDIRMASI
# ============================================================================
def setup_console():
    """Konsol penceresini yapilandirir (baslik, boyut, renk destegi)."""
    s = platform.system().lower()
    if s == "windows":
        try:
            k = ctypes.windll.kernel32
            k.SetConsoleMode(k.GetStdHandle(-11), 7)
        except Exception:
            pass
        os.system("chcp 65001 >nul 2>&1")
        os.system("title NIKO Sistem Temizleyici v3.0")
        # Genis pencere - tum cikti gorunsun
        os.system("mode con: cols=80 lines=55")
    else:
        sys.stdout.write("\033]0;NIKO Sistem Temizleyici v3.0\007")
        sys.stdout.flush()

setup_console()


# ============================================================================
#  ARAYUZ MOTORU
# ============================================================================
class UI:
    """Terminal arayuzu - renkler, paneller, animasyonlar."""

    # -- Renkler --------------------------------------------------------------
    BLUE    = "\033[38;5;33m"
    LBLUE   = "\033[38;5;75m"
    CYAN    = "\033[38;5;80m"
    GREEN   = "\033[38;5;78m"
    LGREEN  = "\033[38;5;114m"
    RED     = "\033[38;5;167m"
    ORANGE  = "\033[38;5;173m"
    YELLOW  = "\033[38;5;222m"
    PURPLE  = "\033[38;5;139m"
    PINK    = "\033[38;5;175m"
    WHITE   = "\033[38;5;255m"
    LGRAY   = "\033[38;5;250m"
    GRAY    = "\033[38;5;243m"
    DGRAY   = "\033[38;5;238m"
    DDGRAY  = "\033[38;5;235m"

    B = "\033[1m"
    D = "\033[2m"
    R = "\033[0m"

    # -- Ikonlar (CMD uyumlu Unicode) -----------------------------------------
    ICON_ARROW  = chr(9658)   # ►
    ICON_DOT    = chr(9679)   # ●
    ICON_CHECK  = chr(8730)   # √
    ICON_CROSS  = chr(215)    # ×
    ICON_STAR   = chr(9733)   # ★
    ICON_DIAMOND = chr(9670)  # ◆
    ICON_SQUARE = chr(9632)   # ■
    ICON_TRI    = chr(9654)   # ▶
    ICON_WARN   = chr(9888)   # ⚠ (works on Win10+)
    ICON_LINE   = chr(9472)   # ─
    ICON_BLOCK  = chr(9608)   # █
    ICON_LBLOCK = chr(9617)   # ░

    @staticmethod
    def clear():
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def type_text(text, color="", delay=0.02):
        """Yazma animasyonu - karakterleri tek tek yazdirir."""
        for ch in text:
            sys.stdout.write(f"{color}{ch}{UI.R}")
            sys.stdout.flush()
            time.sleep(delay)
        print()

    @staticmethod
    def loading_animation(msg, duration=1.0):
        """Yukleme animasyonu - donen cubuk ile."""
        frames = [
            f" {UI.ICON_DOT}     ",
            f"  {UI.ICON_DOT}    ",
            f"   {UI.ICON_DOT}   ",
            f"    {UI.ICON_DOT}  ",
            f"     {UI.ICON_DOT} ",
            f"    {UI.ICON_DOT}  ",
            f"   {UI.ICON_DOT}   ",
            f"  {UI.ICON_DOT}    ",
        ]
        end_time = time.time() + duration
        i = 0
        while time.time() < end_time:
            f = frames[i % len(frames)]
            print(f"\r    {UI.CYAN}{f}{UI.R} {UI.LGRAY}{msg}{UI.R}   ", end="", flush=True)
            time.sleep(0.1)
            i += 1
        print(f"\r{' ' * 70}\r", end="")

    @staticmethod
    def banner():
        """Animasyonlu banner gosterimi."""
        R = UI.R
        B = UI.B
        d = UI.DDGRAY

        # Renk gradyani: mor -> mavi -> cyan
        g = [
            "\033[38;5;97m",
            "\033[38;5;98m",
            "\033[38;5;63m",
            "\033[38;5;69m",
            "\033[38;5;75m",
            "\033[38;5;80m",
            "\033[38;5;81m",
        ]

        lines = [
            (g[0], " ##    ## #### ##    ##  #######  "),
            (g[1], " ###   ##  ##  ##   ##  ##     ## "),
            (g[2], " ####  ##  ##  ##  ##   ##     ## "),
            (g[3], " ## ## ##  ##  #####    ##     ## "),
            (g[4], " ##  ####  ##  ##  ##   ##     ## "),
            (g[5], " ##   ###  ##  ##   ##  ##     ## "),
            (g[6], " ##    ## #### ##    ##  #######  "),
        ]

        print()
        # Ust cerceve
        border = f"    {d}+{'=' * 60}+{R}"
        print(border)
        print(f"    {d}|{R}{' ' * 60}{d}|{R}")

        # Banner satirlarini animasyonlu goster
        for color, art in lines:
            pad = 60 - len(art)
            line = f"    {d}|{R}  {color}{B}{art}{R}{' ' * (pad - 2)}{d}|{R}"
            print(line)
            time.sleep(0.04)  # Satir satir animasyon

        print(f"    {d}|{R}{' ' * 60}{d}|{R}")

        # Alt baslik (yazma animasyonu)
        title = "Sistem Temizleyici v3.0"
        sub = "Windows * macOS * Linux"
        titleline = f"{UI.CYAN}{title}  {UI.DGRAY}|  {UI.PURPLE}{sub}"
        # Merkeze hizala
        raw_len = len(title) + 3 + len(sub)
        pad = 60 - raw_len
        lp = pad // 2
        rp = pad - lp

        print(f"    {d}|{R}{' ' * lp}{titleline}{R}{' ' * rp}{d}|{R}")
        print(f"    {d}|{R}{' ' * 60}{d}|{R}")
        print(border)
        print()

        time.sleep(0.3)

    @staticmethod
    def panel(text, title="SISTEM", color=None):
        """Cerceveli bilgi paneli."""
        if color is None:
            color = UI.LBLUE
        R = UI.R
        B = UI.B
        w = 64

        lines = text.split('\n')

        # Ust kenarlik
        t_part = f" {title} "
        rest = w - len(t_part) - 4
        if rest < 0: rest = 0
        print(f"\n    {color}{B}+--{t_part}{'-' * rest}+{R}")

        for line in lines:
            pad = w - len(line) - 4
            if pad < 0: pad = 0
            print(f"    {color}|{R}  {UI.WHITE}{line}{R}{' ' * pad}  {color}|{R}")

        print(f"    {color}+{'-' * (w - 2)}+{R}")

    @staticmethod
    def progress(cur, total, prefix=""):
        """Animasyonlu ilerleme cubugu."""
        if total == 0: return

        pct = float(cur) * 100 / total
        w = 28
        filled = int(w * cur // total)

        # Renk gecisi
        if pct < 25:    bc = UI.RED
        elif pct < 50:  bc = UI.ORANGE
        elif pct < 75:  bc = UI.YELLOW
        else:           bc = UI.LGREEN

        bar_f = UI.ICON_BLOCK * filled
        bar_e = UI.ICON_LBLOCK * (w - filled)

        sp = ["|", "/", "-", "\\"]
        s = sp[cur % len(sp)]

        # Yuzdeli gosterim
        pct_str = f"{pct:>5.1f}%"

        print(
            f"\r    {UI.PURPLE}{s}{UI.R} "
            f"{UI.LGRAY}{prefix:<16}{UI.R} "
            f"{UI.DGRAY}[{bc}{bar_f}{UI.DGRAY}{bar_e}]{UI.R} "
            f"{bc}{UI.B}{pct_str}{UI.R}",
            end="", flush=True
        )

    @staticmethod
    def step(num, msg):
        """Numarali adim basligi (ikon ile)."""
        print(f"\n    {UI.PURPLE}{UI.ICON_DIAMOND}{UI.R} "
              f"{UI.LBLUE}{UI.B}[{num}]{UI.R} "
              f"{UI.WHITE}{UI.B}{msg}{UI.R}")
        print(f"    {UI.DGRAY}{'.' * 55}{UI.R}")

    @staticmethod
    def info(msg):
        print(f"    {UI.CYAN} {UI.ICON_TRI}{UI.R} {UI.LGRAY}{msg}{UI.R}")

    @staticmethod
    def success(msg):
        print(f"    {UI.GREEN} {UI.ICON_CHECK}{UI.R} {UI.WHITE}{msg}{UI.R}")

    @staticmethod
    def warn(msg):
        print(f"    {UI.ORANGE} {UI.ICON_WARN}{UI.R} {UI.WHITE}{msg}{UI.R}")

    @staticmethod
    def err(msg):
        print(f"    {UI.RED} {UI.ICON_CROSS}{UI.R} {UI.WHITE}{msg}{UI.R}")

    @staticmethod
    def item(path, last=False):
        c = "'" if last else "|"
        print(f"    {UI.DGRAY}    {c}-- {UI.GRAY}{path}{UI.R}")

    @staticmethod
    def line():
        print(f"    {UI.DDGRAY}{UI.ICON_LINE * 55}{UI.R}")

    @staticmethod
    def end_animation():
        """Tamamlanma animasyonu."""
        frames = [
            f"{UI.GREEN}{UI.B}  {UI.ICON_STAR} TAMAMLANDI {UI.ICON_STAR}  {UI.R}",
            f"{UI.LGREEN}{UI.B}  {UI.ICON_STAR} TAMAMLANDI {UI.ICON_STAR}  {UI.R}",
            f"{UI.CYAN}{UI.B}  {UI.ICON_STAR} TAMAMLANDI {UI.ICON_STAR}  {UI.R}",
        ]
        for _ in range(3):
            for f in frames:
                print(f"\r    {f}   ", end="", flush=True)
                time.sleep(0.15)
        print()


# ============================================================================
#  ISLETIM SISTEMI
# ============================================================================
def detect_os():
    s = platform.system().lower()
    return {"windows": "windows", "darwin": "macos", "linux": "linux"}.get(s, "unknown")

def get_os_name(t):
    if t == "windows":
        return f"Windows ({platform.release()}, Build {platform.version()})"
    elif t == "macos":
        v = platform.mac_ver()[0]
        return f"macOS ({v})" if v else "macOS"
    elif t == "linux":
        try:
            import distro
            return f"Linux ({distro.name()} {distro.version()})"
        except ImportError:
            return f"Linux ({platform.release()})"
    return "Bilinmeyen"


# ============================================================================
#  YETKI KONTROL
# ============================================================================
def is_admin():
    if detect_os() == "windows":
        try: return ctypes.windll.shell32.IsUserAnAdmin()
        except: return False
    return os.geteuid() == 0

def run_as_admin():
    if is_admin(): return True
    if detect_os() == "windows":
        try:
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            return False
        except: return False
    print(f"\n    {UI.ORANGE}{UI.ICON_WARN} Root yetkisi gerekli:{UI.R}")
    print(f"    {UI.WHITE}  sudo python3 {sys.argv[0]}{UI.R}\n")
    return False


# ============================================================================
#  TEMIZLIK HEDEFLERI
# ============================================================================
def get_targets(t):
    """Platforma ozel temizlenecek dizinler."""
    targets = []
    if t == "windows":
        tmp = os.environ.get('TEMP')
        if tmp: targets.append(tmp)
        targets.append(r'C:\Windows\Temp')
        targets.append(r'C:\Windows\Prefetch')
        for p in [r'C:\$Recycle.bin', r'C:\Windows\SoftwareDistribution\Download']:
            if os.path.exists(p): targets.append(p)
        la = os.environ.get('LOCALAPPDATA', '')
        if la:
            tc = os.path.join(la, 'Microsoft', 'Windows', 'Explorer')
            if os.path.exists(tc): targets.append(tc)

    elif t == "macos":
        h = Path.home()
        targets += [str(h/"Library"/"Caches"), str(h/"Library"/"Logs"),
                     "/private/var/log", "/private/tmp", "/tmp"]
        for p in [str(h/".Trash"), str(h/"Library"/"Caches"/"Google"/"Chrome")]:
            if os.path.exists(p): targets.append(p)

    elif t == "linux":
        h = Path.home()
        targets += [str(h/".cache"), "/tmp", "/var/tmp", "/var/log"]
        for p in [str(h/".local"/"share"/"Trash"), str(h/".cache"/"thumbnails")]:
            if os.path.exists(p): targets.append(p)

    return [x for x in targets if x and os.path.exists(x)]

def get_logs(t):
    if t == "windows":
        sd = os.environ.get('SystemDrive', 'C:')
        return [f"{sd}/*.log", f"{sd}/Windows/Logs/**/*.log"]
    elif t == "macos":
        return ["/var/log/*.log", f"{Path.home()}/Library/Logs/**/*.log"]
    elif t == "linux":
        return ["/var/log/*.log", "/var/log/**/*.log"]
    return []

def flush_dns(t):
    try:
        if t == "windows":
            subprocess.run(["ipconfig", "/flushdns"], capture_output=True, check=True)
        elif t == "macos":
            subprocess.run(["dscacheutil", "-flushcache"], capture_output=True, check=True)
            subprocess.run(["sudo", "killall", "-HUP", "mDNSResponder"],
                           capture_output=True, check=False)
        elif t == "linux":
            subprocess.run(["systemd-resolve", "--flush-caches"],
                           capture_output=True, check=False)
            subprocess.run(["nscd", "-i", "hosts"], capture_output=True, check=False)
        return True
    except: return False


# ============================================================================
#  ANA TEMIZLIK
# ============================================================================
def clean_system():
    ui = UI()
    start_time = time.time()

    # -- Ekran temizle & banner ----------------------------------------------
    ui.clear()
    ui.banner()

    # -- Sistem bilgisi ------------------------------------------------------
    cur_os = detect_os()
    os_name = get_os_name(cur_os)
    lbl = {"windows": "WIN", "macos": "MAC", "linux": "LNX"}.get(cur_os, "???")

    ui.panel(
        f" [{lbl}]  Isletim Sistemi  :  {os_name}\n"
        f" [PC ]  Makine           :  {platform.node()}\n"
        f" [CPU]  Mimari           :  {platform.machine()}\n"
        f" [PY ]  Python           :  {platform.python_version()}",
        "SISTEM BILGISI",
        ui.LBLUE
    )

    # -- Yetki kontrolu ------------------------------------------------------
    if not is_admin():
        hint = ("Sag tiklayip 'Yonetici olarak calistir' secin."
                if cur_os == "windows"
                else f"Komut: sudo python3 {sys.argv[0]}")
        ui.panel(
            f" HATA: Yonetici yetkisi alinamadi!\n"
            f" {hint}",
            "YETKI HATASI", ui.RED
        )
        time.sleep(3)
        return

    # -- ADIM 1: Hedef tarama ------------------------------------------------
    ui.step(1, "Hedef Dizinler Taraniyor")
    ui.loading_animation("Dizinler kontrol ediliyor...", 0.8)

    targets = get_targets(cur_os)
    for i, t in enumerate(targets):
        ui.item(t, last=(i == len(targets) - 1))
        time.sleep(0.05)  # Kisa animasyon

    ui.info(f"{len(targets)} hedef dizin tespit edildi.")

    # -- ADIM 2: Dosya analizi -----------------------------------------------
    ui.step(2, "Dosyalar Analiz Ediliyor")
    ui.loading_animation("Dosyalar taranıyor...", 1.0)

    all_files = []
    total_bytes = 0

    for t in targets:
        if t and os.path.exists(t):
            for root, dirs, files in os.walk(t):
                for name in files:
                    fp = os.path.join(root, name)
                    all_files.append(fp)
                    try: total_bytes += os.path.getsize(fp)
                    except: pass
                for name in dirs:
                    all_files.append(os.path.join(root, name))

    for pat in get_logs(cur_os):
        for lf in glob.glob(pat, recursive=True):
            if lf not in all_files:
                all_files.append(lf)
                try: total_bytes += os.path.getsize(lf)
                except: pass

    size_mb = round(total_bytes / (1024 * 1024), 2)
    ui.success(f"{len(all_files)} oge bulundu  |  {size_mb} MB")

    # -- ADIM 3: Temizlik ----------------------------------------------------
    ui.step(3, "Temizlik Islemi Baslatiliyor")

    if not all_files:
        ui.warn("Silinecek dosya bulunamadi!")
    else:
        deleted = 0
        failed = 0

        for i, item in enumerate(all_files, 1):
            try:
                if os.path.isfile(item) or os.path.islink(item):
                    os.unlink(item)
                    deleted += 1
                elif os.path.isdir(item):
                    shutil.rmtree(item, ignore_errors=True)
                    deleted += 1
            except:
                failed += 1

            if i % 5 == 0 or i == len(all_files):
                ui.progress(i, len(all_files), "Temizleniyor...")

        print("\n")
        ui.success(f"{deleted} oge silindi.")
        if failed > 0:
            ui.warn(f"{failed} oge atlandi (kilitli).")

    # -- ADIM 4: DNS ---------------------------------------------------------
    ui.step(4, "DNS Onbellegi")
    ui.loading_animation("DNS temizleniyor...", 0.6)

    if flush_dns(cur_os):
        ui.success("DNS onbellegi temizlendi.")
    else:
        ui.warn("DNS temizlenemedi.")

    # -- OZET ----------------------------------------------------------------
    elapsed = round(time.time() - start_time, 1)
    now = datetime.now().strftime('%H:%M:%S')

    print()
    ui.end_animation()

    ui.panel(
        f" {UI.ICON_STAR} ISLEM BASARIYLA TAMAMLANDI!\n"
        f"\n"
        f" {UI.ICON_TRI} Temizlenen alan   :  ~{size_mb} MB\n"
        f" {UI.ICON_TRI} Islenen oge        :  {len(all_files)}\n"
        f" {UI.ICON_TRI} Isletim sistemi    :  {os_name}\n"
        f" {UI.ICON_TRI} Sure               :  {elapsed} saniye\n"
        f" {UI.ICON_TRI} Saat               :  {now}",
        "OZET RAPOR", ui.GREEN
    )

    print(f"\n    {ui.GRAY}Kapatmak icin Enter tusuna basin...{ui.R}")
    input()


# ============================================================================
#  GIRIS NOKTASI
# ============================================================================
if __name__ == "__main__":
    cur = detect_os()

    if cur == "unknown":
        print(f"\n    ! Desteklenmeyen sistem: {platform.system()}")
        print("    Windows, macOS veya Linux gerekli.\n")
    elif cur == "windows":
        if is_admin():
            clean_system()
        else:
            print("    ... Yonetici yetkisi isteniyor...")
            if not run_as_admin(): sys.exit(0)
    else:
        if is_admin():
            clean_system()
        else:
            print(f"\n    {UI.ORANGE}{UI.ICON_WARN} Root yetkisi gerekli!{UI.R}")
            print(f"    {UI.WHITE}  sudo python3 {sys.argv[0]}{UI.R}\n")
            sys.exit(1)
