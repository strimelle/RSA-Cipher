# RSA Cipher Application

A Python desktop application for RSA text encryption and decryption with a Tkinter graphical user interface.

## Features

- Enter plaintext and encrypt it using RSA
- Decrypt encrypted RSA message
- Input prime numbers `p` and `q`
- Automatic calculation of:
  - `n = p * q`
  - `phi = (p - 1) * (q - 1)`
- Extended Euclidean Algorithm for modular inverse
- RSA encryption and decryption logic implemented manually
- Open text from file
- Save output to file
- Simple Tkinter GUI

## Project Structure

main.py  
rsa_logic.py  
file_util.py  
README.md

## File Descriptions

- `main.py` – graphical user interface and button logic
- `rsa_logic.py` – RSA calculations, encryption, decryption, prime checking
- `file_util.py` – file open/save functions

## Technologies Used

- Python
- Tkinter

## RSA Logic

The application uses the RSA algorithm:

1. The user enters two prime numbers `p` and `q`
2. The program calculates:
   - `n = p * q`
   - `phi = (p - 1) * (q - 1)`
3. A valid public exponent `e` is selected
4. The private exponent `d` is calculated using the Extended Euclidean Algorithm
5. Encryption formula:
   - `c = m^e mod n`
6. Decryption formula:
   - `m = c^d mod n`

## How to Run

1. Make sure Python is installed
2. Download or clone the repository
3. Open the project folder
4. Run:

python main.py

## How to Use

### Encryption

1. Enter a message
2. Enter prime numbers `p` and `q`
3. Select **Encrypt**
4. Click **GO!**
5. The encrypted output will appear in the output window

### Decryption

1. Enter the encrypted list of numbers
2. Enter the same prime numbers `p` and `q`
3. Select **Decrypt**
4. Click **GO!**
5. The decrypted text will appear in the output window

## Example Test Data

### Encryption test

- Message: `LABAS`
- `p = 61`
- `q = 53`

Expected encrypted output:

[2726, 2790, 524, 2790, 2680]

### Decryption test

- Message: `[2726, 2790, 524, 2790, 2680]`
- `p = 61`
- `q = 53`

Expected decrypted output:

LABAS

## Notes

- `p` and `q` must be prime numbers
- The same `p` and `q` values must be used for both encryption and decryption
- The project is intended for educational purposes

## Author

Created as a university practical assignment on RSA encryption and decryption.