# 🧬 Genetic Encryption Algorithm 🔒

This project implements a robust **Genetic Encryption Algorithm** 🧬 that offers both encryption 🔒 and decryption 🔓 functionalities with dynamic key generation 🔑. The algorithm cleverly combines DNA base mapping 🗺️ and polynomial interpolation 📊 to generate secure and unique keys.

<p align="center">
  <a href="#english-section">🇬🇧 English</a> | <a href="#turkish-section">🇹🇷 Türkçe</a>
</p>

---

## 🇬🇧 English Section <a name="english-section"></a>

### ✨ Features

*   **🌍 Language Support**: Available in both English and Turkish.
*   **🔑 Dynamic Key Generation**: Keys are uniquely generated based on user input and the system's timestamp, ensuring each encryption is distinct.
*   **🛡️ Initialization Vector (IV)**: Employs a unique IV for every encryption process, adding an extra layer of security.
*   **🧬 DNA Base Mapping**: Transforms numerical data into DNA sequences, introducing biological complexity to the encryption.

### ⚙️ Prerequisites

Make sure you have the following libraries installed. The script will attempt to install them automatically if they are missing:

*   `colorama` 🎨
*   `sympy` 🧮

### 🚀 How to Run

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Woffluon/genetic-encryption.git
    cd genetic-encryption
    ```
2.  **Execute the script:**
    ```bash
    python algorithm.py
    ```
3.  **Choose your language** (English/Türkçe) by entering `1` or `2`.
4.  **Select an action:**
    *   `1` for Encrypt 🔒
    *   `2` for Decrypt 🔓
5.  **Follow the prompts** to enter your open key and the text you wish to encrypt or decrypt.

### 🗂️ File Structure

*   `algorithm.py`: The main Python script containing the encryption and decryption algorithm.
*   `Algorithm_gui.py`: A Python script providing a Graphical User Interface (GUI) for the algorithm.
*   `README.md`: This documentation file, providing details about the project.

### 💡 Example Usage

#### 🔒 Encryption

1.  Choose the **Encrypt** option (`1`).
2.  Enter your **open key** when prompted.
3.  Input the **plaintext** you want to encrypt.
4.  The **encrypted text** will be displayed in the console.

#### 🔓 Decryption

1.  Choose the **Decrypt** option (`2`).
2.  Enter the **open key** you used for encryption.
3.  Input the **ciphertext** you want to decrypt.
4.  The **decrypted text** will be shown in the console.

### 🙌 Contributions

Contributions are highly appreciated! To contribute to this project:

1.  **Fork** the repository to your own GitHub account.
2.  **Create a new branch** for your feature or bug fix:
    ```bash
    git checkout -b feature-name
    ```
3.  **Commit your changes** with descriptive commit messages:
    ```bash
    git commit -m "✨ Add a new feature"
    ```
4.  **Push your branch** to your forked repository:
    ```bash
    git push origin feature-name
    ```
5.  **Open a Pull Request** on the original repository.

### 📜 License

This project is licensed under the MIT License. For more details, please see the `LICENSE` file.

---

## 🇹🇷 Türkçe Bölüm <a name="turkish-section"></a>

### ✨ Özellikler

*   **🌍 Dil Desteği**: Hem İngilizce hem de Türkçe dil seçenekleri mevcuttur.
*   **🔑 Dinamik Anahtar Üretimi**: Anahtarlar, kullanıcı girdisine ve sistem zaman damgasına göre benzersiz bir şekilde üretilir, bu da her şifrelemenin farklı olmasını sağlar.
*   **🛡️ Başlangıç Vektörü (IV)**: Her şifreleme işlemi için benzersiz bir IV kullanır, bu da ekstra bir güvenlik katmanı ekler.
*   **🧬 DNA Baz Eşleme**: Sayısal verileri DNA dizilerine dönüştürerek şifrelemeye biyolojik bir karmaşıklık katar.

### ⚙️ Gereksinimler

Aşağıdaki kütüphanelerin kurulu olduğundan emin olun. Eğer eksikse, komut dosyası bunları otomatik olarak yüklemeye çalışacaktır:

*   `colorama` 🎨
*   `sympy` 🧮

### 🚀 Nasıl Çalıştırılır

1.  **Depoyu klonlayın:**
    ```bash
    git clone https://github.com/Woffluon/genetic-encryption.git
    cd genetic-encryption
    ```
2.  **Komut dosyasını çalıştırın:**
    ```bash
    python algorithm.py
    ```
3.  **Dilinizi seçin** (İngilizce/Türkçe) `1` veya `2` girerek.
4.  **Bir işlem seçin:**
    *   `1` Şifrele 🔒
    *   `2` Şifre Çöz 🔓
5.  **İstenenleri takip ederek** açık anahtarınızı ve şifrelemek veya çözmek istediğiniz metni girin.

### 🗂️ Dosya Yapısı

*   `algorithm.py`: Şifreleme ve çözme algoritmasını içeren ana Python komut dosyası.
*   `Algorithm_gui.py`: Algoritma için Grafik Kullanıcı Arayüzü (GUI) sağlayan bir Python komut dosyası.
*   `README.md`: Proje hakkında detaylı bilgi veren bu dokümantasyon dosyası.

### 💡 Örnek Kullanım

#### 🔒 Şifreleme

1.  **Şifrele** seçeneğini (`1`) seçin.
2.  İstendiğinde **açık anahtarınızı** girin.
3.  Şifrelemek istediğiniz **düz metni** girin.
4.  **Şifrelenmiş metin** konsolda görüntülenecektir.

#### 🔓 Şifre Çözme

1.  **Şifre Çöz** seçeneğini (`2`) seçin.
2.  Şifreleme için kullandığınız **açık anahtarı** girin.
3.  Çözmek istediğiniz **şifreli metni** girin.
4.  **Çözülmüş metin** konsolda gösterilecektir.

### 🙌 Katkılar

Katkılarınız memnuniyetle karşılanır! Bu projeye katkıda bulunmak için:

1.  Depoyu kendi GitHub hesabınıza **fork** edin.
2.  Özelliğiniz veya hata düzeltmeniz için **yeni bir dal oluşturun**:
    ```bash
    git checkout -b feature-adı
    ```
3.  **Değişikliklerinizi** açıklayıcı commit mesajlarıyla **commit edin**:
    ```bash
    git commit -m "✨ Yeni bir özellik ekle"
    ```
4.  **Dalınızı** kendi forkladığınız depoya **push edin**:
    ```bash
    git push origin feature-adı
    ```
5.  Orijinal depoda **Çekme İsteği (Pull Request)** açın.

### 📜 Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla detay için lütfen `LICENSE` dosyasına bakın.
