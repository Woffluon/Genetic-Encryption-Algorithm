# Genetic Encryption Algorithm

This project implements a **Genetic Encryption Algorithm** that provides both encryption and decryption functionalities with dynamic key generation. The algorithm uses concepts like DNA base mapping and polynomial interpolation to create secure and unique keys.

## Features

- **Language Support**: English and Turkish
- **Dynamic Key Generation**: Keys are generated based on input and system timestamp.
- **Initialization Vector (IV)**: Each encryption uses a unique IV.
- **DNA Base Mapping**: Converts numerical data into DNA sequences for additional complexity.

## Prerequisites

Ensure the following libraries are installed:

- `colorama`
- `sympy`

If not, the script will automatically install them.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Woffluon/genetic-encryption.git
   cd genetic-encryption
   ```
2. Run the script:
   ```bash
   python algorithm.py
   ```
3. Choose the language (English/Türkçe).
4. Select an action:
   - Encrypt
   - Decrypt
5. Provide the required inputs, such as the open key and plaintext or ciphertext.

## File Structure

- `algorithm.py`: Main script implementing the algorithm.
- `README.md`: Documentation for the project.

## Example Usage

### Encryption

1. Select the **Encrypt** option.
2. Enter the open key and plaintext.
3. The encrypted text will be displayed.

### Decryption

1. Select the **Decrypt** option.
2. Enter the open key and ciphertext.
3. The decrypted text will be displayed.

## Contributions

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

