# ShadowBits

**ShadowBits** is a Python-based steganography tool designed for cybersecurity purposes. It uses the **Least Significant Bit (LSB)** technique to hide and extract text messages within PNG images.

The goal of this project is to demonstrate how data can be covertly embedded in digital images while maintaining visual integrity, a concept commonly studied in information security, digital forensics, and malware analysis.

---

## Features

* Hide text messages inside PNG images using LSB steganography
* Extract hidden messages from modified images
* Simple command-line interface (CLI)
* Lightweight and easy to understand
* Ideal for academic projects and cybersecurity demonstrations

---

## Requirements

* Python **3.8+**
* Git
* Virtual environment support (`venv`)

---

## Clone the Repository

```bash
git clone https://github.com/alisster00/shadowbits.git
cd shadowbits
```

---

## Create and Activate a Virtual Environment

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```powershell
python -m venv venv
venv\Scripts\activate
```

Once activated, your terminal prompt should indicate that the virtual environment is active.

---

## Install Dependencies

ShadowBits depends on the **Pillow** library for image processing.

```bash
pip install pillow
```

---

## Usage

ShadowBits supports two modes:

* **H** → Hide a message inside an image
* **E** → Extract a hidden message from an image

### Hide a Message

```bash
python shadowbits.py H -i input.png -o output.png -m "Secret message"
```

**Parameters:**

* `-i / --input` → Input PNG image
* `-o / --output` → Output image with hidden message
* `-m / --message` → Message to hide

---

### Extract a Message

```bash
python shadowbits.py E -i output.png
```

The hidden message will be printed to the terminal.

---

## How It Works

1. The input image is converted to RGB format
2. The text message is converted to binary (8 bits per character)
3. Each bit is embedded into the **least significant bit** of the RGB channels
4. A null byte (`00000000`) marks the end of the message
5. During extraction, LSBs are read sequentially and converted back to text

This technique minimizes visual distortion and keeps the image appearance nearly identical to the original.

---

## Limitations

* Only supports **PNG images**
* Messages are not encrypted
* Large messages may exceed image capacity

---

## Security Considerations

ShadowBits is intended for **educational and research purposes only**. It does not implement encryption or anti-forensic techniques. For real-world secure communication, combine steganography with cryptographic methods.

---

## Use Cases

* Cybersecurity education
* Digital forensics research
* Steganography demonstrations
* CTF challenges
* Proof-of-concept covert channels


