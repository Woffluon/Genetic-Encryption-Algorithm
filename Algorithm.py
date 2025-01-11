import subprocess
import sys
import os
import time
import base64
import random
from datetime import datetime
from colorama import Fore, Style, init
from sympy import symbols

required_libraries = ["colorama", "sympy"]
for library in required_libraries:
    try:
        __import__(library)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", library])

init(autoreset=True)

DNA_MAP = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}

def polynomial_iteration(seed, degree=3):
    x = symbols('x')
    return [x**i + seed for i in range(degree)]

def lagrange_interpolation(points):
    x = symbols('x')
    n = len(points)
    polynomial = 0
    for i in range(n):
        xi, yi = points[i]
        term = yi
        for j in range(n):
            if i != j:
                xj = points[j][0]
                term *= (x - xj) / (xi - xj)
        polynomial += term
    return polynomial

def generate_long_random_key(length=64):
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', k=length))

def to_base_4(value):
    result = ""
    while value > 0:
        result = str(value % 4) + result
        value //= 4
    return result.zfill(4)

def generate_key(open_key, timestamp):
    seed = sum(ord(char) for char in open_key) + sum(timestamp)
    polynomials = polynomial_iteration(seed)
    points = [(i, p.subs('x', i)) for i, p in enumerate(polynomials)]
    interpolation = lagrange_interpolation(points)

    day, month, year, hour, minute = timestamp
    formatted_time = [day, month, year % 100, year // 100, hour, minute]
    ascii_values = [ord(char) for char in open_key]
    combined = [(ascii_values[i % len(ascii_values)] + formatted_time[i % len(formatted_time)]) for i in range(len(ascii_values))]
    base_4_values = [to_base_4(value) for value in combined]
    dna_sequence = ''.join(DNA_MAP[int(digit)] for value in base_4_values for digit in value)
    codons = [dna_sequence[i:i+3] for i in range(0, len(dna_sequence), 3)]
    return [sum(ord(char) for char in codon) % 100 for codon in codons]

def generate_iv(length=16):
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', k=length))

def encrypt(plaintext, key):
    iv = generate_iv(16)
    encrypted = ''.join(chr(ord(char) ^ key[i % len(key)] ^ ord(iv[i % len(iv)])) for i, char in enumerate(plaintext))
    return base64.urlsafe_b64encode(f"{iv}:{encrypted}".encode()).decode()

def decrypt(ciphertext, key):
    decoded_data = base64.urlsafe_b64decode(ciphertext).decode()
    iv, encrypted_text = decoded_data.split(':', 1)
    return ''.join(chr(ord(char) ^ key[i % len(key)] ^ ord(iv[i % len(iv)])) for i, char in enumerate(encrypted_text))

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome_screen(language):
    clear_console()
    if language == "en":
        print(f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}" + "-"*50)
        print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}       GENETIC ENCRYPTION ALGORITHM")
        print(f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}" + "-"*50)
    else:
        print(f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}" + "-"*50)
        print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}         GENETİK ŞİFRELEME ALGORİTMASI")
        print(f"{Fore.LIGHTYELLOW_EX}{Style.BRIGHT}" + "-"*50)

def get_system_time():
    now = datetime.now()
    return now.day, now.month, now.year, now.hour, now.minute

def main():
    print("1: English")
    print("2: Türkçe")
    language = input("Select Language / Dil Seçin (1/2): ").strip()
    if language == "1":
        language = "en"
    elif language == "2":
        language = "tr"
    else:
        print("Invalid choice, defaulting to English")
        language = "en"

    while True:
        welcome_screen(language)
        if language == "en":
            print("1: Encrypt")
            print("2: Decrypt")
            action_prompt = "Choose an action (1/2): "
            key_prompt = "Enter Open Key: "
            text_encrypt_prompt = "Enter text to encrypt: "
            text_decrypt_prompt = "Enter text to decrypt: "
            encrypted_message = "Encrypted Text: "
            decrypted_message = "Decrypted Text: "
            continue_prompt = "Press ENTER to continue..."
        else:
            print("1: Şifrelemek için")
            print("2: Çözmek için")
            action_prompt = "Bir işlem seçin (1/2): "
            key_prompt = "Açık Anahtar Girin: "
            text_encrypt_prompt = "Şifrelenecek metni girin: "
            text_decrypt_prompt = "Çözülecek metni girin: "
            encrypted_message = "Şifrelenmiş Metin: "
            decrypted_message = "Çözülen Metin: "
            continue_prompt = "Devam etmek için ENTER'a basın..."

        action = input(action_prompt).strip()
        if action not in ['1', '2']:
            print(Fore.RED + "Invalid action. Please choose 1 or 2." if language == "en" else "Geçersiz işlem seçimi. Lütfen 1 veya 2 yazın.")
            continue

        open_key = input(key_prompt).strip()
        timestamp = get_system_time()
        key = generate_key(open_key, timestamp)

        if action == '1':
            plaintext = input(text_encrypt_prompt)
            encrypted_text = encrypt(plaintext, key)
            print(Fore.LIGHTGREEN_EX + encrypted_message + encrypted_text)
        elif action == '2':
            ciphertext = input(text_decrypt_prompt)
            decrypted_text = decrypt(ciphertext, key)
            print(Fore.LIGHTGREEN_EX + decrypted_message + decrypted_text)

        input(Fore.LIGHTCYAN_EX + continue_prompt)

if __name__ == "__main__":
    main()
