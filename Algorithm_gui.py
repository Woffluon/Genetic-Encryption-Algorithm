import tkinter as tk
from tkinter import ttk, scrolledtext
import os
import time
import base64
import random
from datetime import datetime
from typing import Tuple, List
from sympy import symbols

DNA_MAP = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}

TRANSLATIONS = {
    'en': {
        'title': 'Genetic Encryption',
        'mode': 'Mode',
        'encrypt': 'Encrypt',
        'decrypt': 'Decrypt',
        'open_key': 'Open Key:',
        'text_to_encrypt': 'Text to Encrypt:',
        'text_to_decrypt': 'Text to Decrypt:',
        'result': 'Result:',
        'copy_result': 'Copy Result',
        'error': 'Error',
        'fill_fields': 'Please fill in all fields',
        'processing_error': 'Error processing text: {}',
        'ok': 'OK'
    },
    'tr': {
        'title': 'Genetik Şifreleme',
        'mode': 'Mod',
        'encrypt': 'Şifrele',
        'decrypt': 'Şifre Çöz',
        'open_key': 'Açık Anahtar:',
        'text_to_encrypt': 'Şifrelenecek Metin:',
        'text_to_decrypt': 'Çözülecek Metin:',
        'result': 'Sonuç:',
        'copy_result': 'Sonucu Kopyala',
        'error': 'Hata',
        'fill_fields': 'Lütfen tüm alanları doldurun',
        'processing_error': 'Metin işleme hatası: {}',
        'ok': 'Tamam'
    }
}

def polynomial_iteration(seed, degree=3):
    x = symbols('x')
    polynomials = []
    for i in range(degree):
        polynomials.append(x**i + seed)
    return polynomials

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
    key = [sum(ord(char) for char in codon) % 100 for codon in codons]
    return key

def generate_iv(length=16):
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', k=length))

def encrypt(plaintext, key):
    iv = generate_iv(16)
    encrypted = ''.join(chr(ord(char) ^ key[i % len(key)] ^ ord(iv[i % len(iv)])) for i, char in enumerate(plaintext))
    encoded_result = base64.urlsafe_b64encode(f"{iv}:{encrypted}".encode()).decode()
    return encoded_result

def decrypt(ciphertext, key):
    try:
        decoded_data = base64.urlsafe_b64decode(ciphertext).decode()
        iv, encrypted_text = decoded_data.split(':', 1)
        decrypted = ''.join(chr(ord(char) ^ key[i % len(key)] ^ ord(iv[i % len(iv)])) for i, char in enumerate(encrypted_text))
        return decrypted
    except:
        return "Decryption failed. Please check your input and key."

class GeneticEncryptionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Genetic Encryption / Genetik Şifreleme")
        self.root.geometry("800x650") 
        
        self.current_lang = tk.StringVar(value='tr')
        
        self.style = ttk.Style()
        self.style.configure('TButton', padding=10)
        self.style.configure('Header.TLabel', font=('Helvetica', 24, 'bold'))
        self.style.configure('Mode.TButton', padding=10, width=20)
        
        self.setup_ui()
        
    def setup_ui(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        lang_frame = ttk.Frame(main_frame)
        lang_frame.grid(row=0, column=0, columnspan=2, pady=(0, 10))
        
        ttk.Radiobutton(
            lang_frame,
            text="Türkçe",
            value="tr",
            variable=self.current_lang,
            command=self.update_language
        ).pack(side=tk.LEFT, padx=10)
        
        ttk.Radiobutton(
            lang_frame,
            text="English",
            value="en",
            variable=self.current_lang,
            command=self.update_language
        ).pack(side=tk.LEFT, padx=10)
        
        self.header = ttk.Label(
            main_frame, 
            style='Header.TLabel'
        )
        self.header.grid(row=1, column=0, columnspan=2, pady=(0, 20))
        
        self.mode_frame = ttk.LabelFrame(main_frame, padding="10")
        self.mode_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))
        
        self.mode_var = tk.StringVar(value="encrypt")
        self.encrypt_btn = ttk.Radiobutton(
            self.mode_frame, 
            value="encrypt", 
            variable=self.mode_var,
            command=self.update_mode
        )
        self.decrypt_btn = ttk.Radiobutton(
            self.mode_frame, 
            value="decrypt", 
            variable=self.mode_var,
            command=self.update_mode
        )
        
        self.encrypt_btn.grid(row=0, column=0, padx=10)
        self.decrypt_btn.grid(row=0, column=1, padx=10)
        
        self.open_key_label = ttk.Label(main_frame)
        self.open_key_label.grid(row=3, column=0, sticky=tk.W, pady=(0, 5))
        
        self.open_key_entry = ttk.Entry(main_frame)
        self.open_key_entry.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.input_label = ttk.Label(main_frame)
        self.input_label.grid(row=4, column=0, sticky=tk.W, pady=(0, 5))
        
        self.input_text = scrolledtext.ScrolledText(
            main_frame, 
            height=6, 
            width=50, 
            wrap=tk.WORD
        )
        self.input_text.grid(row=4, column=1, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.process_btn = ttk.Button(
            main_frame,
            command=self.process_text,
            style='TButton'
        )
        self.process_btn.grid(row=5, column=0, columnspan=2, pady=(0, 20))
        
        self.result_label = ttk.Label(main_frame)
        self.result_label.grid(row=6, column=0, sticky=tk.W, pady=(0, 5))
        
        self.result_text = scrolledtext.ScrolledText(
            main_frame, 
            height=6, 
            width=50, 
            wrap=tk.WORD
        )
        self.result_text.grid(row=6, column=1, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.copy_btn = ttk.Button(
            main_frame,
            command=self.copy_result,
            style='TButton'
        )
        self.copy_btn.grid(row=7, column=0, columnspan=2)
        
        self.update_language()
        
    def update_language(self):
        lang = self.current_lang.get()
        texts = TRANSLATIONS[lang]
        
        self.root.title(texts['title'])
        self.header.config(text=texts['title'])
        self.mode_frame.config(text=texts['mode'])
        self.encrypt_btn.config(text=texts['encrypt'])
        self.decrypt_btn.config(text=texts['decrypt'])
        self.open_key_label.config(text=texts['open_key'])
        self.process_btn.config(text=texts['encrypt'] if self.mode_var.get() == 'encrypt' else texts['decrypt'])
        self.result_label.config(text=texts['result'])
        self.copy_btn.config(text=texts['copy_result'])
        
        self.input_label.config(
            text=texts['text_to_encrypt'] if self.mode_var.get() == 'encrypt' else texts['text_to_decrypt']
        )
        
    def update_mode(self):
        self.input_text.delete("1.0", tk.END)
        self.result_text.delete("1.0", tk.END)
        
        lang = self.current_lang.get()
        texts = TRANSLATIONS[lang]
        mode = self.mode_var.get()
        
        self.input_label.config(
            text=texts['text_to_encrypt'] if mode == 'encrypt' else texts['text_to_decrypt']
        )
        self.process_btn.config(
            text=texts['encrypt'] if mode == 'encrypt' else texts['decrypt']
        )
            
    def process_text(self):
        mode = self.mode_var.get()
        input_text = self.input_text.get("1.0", tk.END).strip()
        open_key = self.open_key_entry.get()
        
        lang = self.current_lang.get()
        texts = TRANSLATIONS[lang]
        
        if not input_text or not open_key:
            self.show_error(texts['fill_fields'])
            return
        
        now = datetime.now()
        timestamp = (now.day, now.month, now.year, now.hour, now.minute)
        
        key = generate_key(open_key, timestamp)
        
        try:
            if mode == "encrypt":
                result = encrypt(input_text, key)
            else:
                result = decrypt(input_text, key)
                
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert("1.0", result)
        except Exception as e:
            self.show_error(texts['processing_error'].format(str(e)))
        
    def copy_result(self):
        result = self.result_text.get("1.0", tk.END).strip()
        self.root.clipboard_clear()
        self.root.clipboard_append(result)
        
    def show_error(self, message):
        lang = self.current_lang.get()
        texts = TRANSLATIONS[lang]
        
        error_window = tk.Toplevel(self.root)
        error_window.title(texts['error'])
        error_window.geometry("300x100")
        
        ttk.Label(
            error_window,
            text=message,
            wraplength=250
        ).pack(pady=20)
        
        ttk.Button(
            error_window,
            text=texts['ok'],
            command=error_window.destroy
        ).pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = GeneticEncryptionGUI(root)
    root.mainloop()