# 🧬🔒 Genetik Şifreleme Algoritması / Genetic Encryption Algorithm 🧬🔒

Bu proje, dinamik anahtar üretimi ile hem şifreleme hem de şifre çözme işlevselliği sağlayan bir **Genetik Şifreleme Algoritması** uygular. Algoritma, güvenli ve benzersiz anahtarlar oluşturmak için DNA baz eşleme ve polinom interpolasyonu gibi kavramları kullanır.

---

This project implements a **Genetic Encryption Algorithm** that provides both encryption and decryption functionalities with dynamic key generation. The algorithm uses concepts like DNA base mapping and polynomial interpolation to create secure and unique keys.

## ✨ Özellikler / Features ✨

- **🌐 Dil Desteği / Language Support**: İngilizce ve Türkçe / English and Turkish
- **🔑 Dinamik Anahtar Üretimi / Dynamic Key Generation**: Anahtarlar girdi ve sistem zaman damgasına göre üretilir. / Keys are generated based on input and system timestamp.
- **🛡️ Başlangıç Vektörü (IV) / Initialization Vector (IV)**: Her şifreleme benzersiz bir IV kullanır. / Each encryption uses a unique IV.
- **🧬 DNA Baz Eşleme / DNA Base Mapping**: Sayısal verileri ek karmaşıklık için DNA dizilerine dönüştürür. / Converts numerical data into DNA sequences for additional complexity.

---

- **🌐 Language Support**: English and Turkish
- **🔑 Dynamic Key Generation**: Keys are generated based on input and system timestamp.
- **🛡️ Initialization Vector (IV)**: Each encryption uses a unique IV.
- **🧬 DNA Base Mapping**: Converts numerical data into DNA sequences for additional complexity.

## ✅ Ön Gereksinimler / Prerequisites ✅

Aşağıdaki kütüphanelerin kurulu olduğundan emin olun:

- `colorama`
- `sympy`

Eğer kurulu değilse, komut dosyası bunları otomatik olarak kuracaktır.

---

Ensure the following libraries are installed:

- `colorama`
- `sympy`

If not, the script will automatically install them.

## 🚀 Nasıl Çalıştırılır / How to Run 🚀

1.  Depoyu klonlayın:
    ```bash
    git clone https://github.com/Woffluon/genetic-encryption.git
    cd genetic-encryption
    ```
2.  Komut dosyasını çalıştırın:
    ```bash
    python algorithm.py
    ```
3.  Dili seçin (İngilizce/Türkçe). / Choose the language (English/Türkçe).
4.  Bir eylem seçin: / Select an action:
    - Şifrele / Encrypt
    - Şifre Çöz / Decrypt
5.  Açık anahtar ve düz metin veya şifreli metin gibi gerekli girdileri sağlayın. / Provide the required inputs, such as the open key and plaintext or ciphertext.

---

1.  Clone the repository:
    ```bash
    git clone https://github.com/Woffluon/genetic-encryption.git
    cd genetic-encryption
    ```
2.  Run the script:
    ```bash
    python algorithm.py
    ```
3.  Choose the language (English/Türkçe).
4.  Select an action:
    - Encrypt
    - Decrypt
5.  Provide the required inputs, such as the open key and plaintext or ciphertext.

## 🗂️ Dosya Yapısı / File Structure 🗂️

- `algorithm.py`: Algoritmayı uygulayan ana komut dosyası. / Main script implementing the algorithm.
- `Algorithm_gui.py`: Tkinter ile GUI arayüzü. / GUI interface with Tkinter.
- `README.md`: Proje için dokümantasyon. / Documentation for the project.

---

- `algorithm.py`: Main script implementing the algorithm.
- `Algorithm_gui.py`: GUI interface with Tkinter.
- `README.md`: Documentation for the project.

## 💡 Örnek Kullanım / Example Usage 💡

### Şifreleme / Encryption

1.  **Şifrele / Encrypt** seçeneğini seçin. / Select the **Encrypt** option.
2.  Açık anahtarı ve düz metni girin. / Enter the open key and plaintext.
3.  Şifrelenmiş metin görüntülenecektir. / The encrypted text will be displayed.

### Şifre Çözme / Decryption

1.  **Şifre Çöz / Decrypt** seçeneğini seçin. / Select the **Decrypt** option.
2.  Açık anahtarı ve şifreli metni girin. / Enter the open key and ciphertext.
3.  Şifresi çözülmüş metin görüntülenecektir. / The decrypted text will be displayed.

---

### Encryption

1.  Select the **Encrypt** option.
2.  Enter the open key and plaintext.
3.  The encrypted text will be displayed.

### Decryption

1.  Select the **Decrypt** option.
2.  Enter the open key and ciphertext.
3.  The decrypted text will be displayed.

## 🤝 Katkılar / Contributions 🤝

Katkılar memnuniyetle karşılanır! Katkıda bulunmak için:

1.  Depoyu çatallayın. / Fork the repository.
2.  Yeni bir dal oluşturun: / Create a new branch:
    ```bash
    git checkout -b feature-name
    ```
3.  Değişikliklerinizi kaydedin: / Commit your changes:
    ```bash
    git commit -m "Özellik ekle / Add feature"
    ```
4.  Dalınıza gönderin: / Push to your branch:
    ```bash
    git push origin feature-name
    ```
5.  Bir çekme isteği açın. / Open a pull request.

---

Contributions are welcome! To contribute:

1.  Fork the repository.
2.  Create a new branch:
    ```bash
    git checkout -b feature-name
    ```
3.  Commit your changes:
    ```bash
    git commit -m "Add feature"
    ```
4.  Push to your branch:
    ```bash
    git push origin feature-name
    ```
5.  Open a pull request.

## 📜 Lisans / License 📜

Bu proje MIT Lisansı altında lisanslanmıştır. Ayrıntılar için `LICENSE` dosyasına bakın.

---

This project is licensed under the MIT License. See the `LICENSE` file for details.
