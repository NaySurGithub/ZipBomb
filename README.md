# Zip Bomb (Educational Purpose Only)

## Introduction

A **zip bomb** is a malicious file used to overload or crash file decompression software by exploiting the way compressed files are handled. The goal of this project is purely educational and to demonstrate how compression algorithms can be used in unintended ways.

### Disclaimer

This project is **not** intended for malicious use. It is created solely for **educational purposes** to help understand the vulnerabilities and risks associated with file compression. Misuse of this code, including creating or distributing zip bombs with harmful intent, is illegal and unethical. Please act responsibly and respect the privacy and security of others.

### How It Works

A zip bomb works by nesting multiple layers of compressed files, each containing further compressed files. This can result in extremely large files once decompressed, overwhelming the system's resources and causing issues such as:

- High CPU usage
- Memory overload
- System crashes

This project demonstrates how these zip bombs are created and why they are dangerous.

## How to Use

```bash
1. **Clone the Repository**
   git clone https://github.com/yourusername/zipbomb.git
   cd zipbomb
2. **Generate the Zip Bomb**
   The script `generate_zip_bomb.py` will create a zip bomb. This script allows you to configure the number of layers, files per layer, and the size of the payload.

   Example to generate a zip bomb with 5 layers, 10 files per layer, and a 100GB payload:
   python generate_zip_bomb.py ```

   **Important:** Do not run this on systems you do not own or have explicit permission to test.
This code can generate **large files** that can cause **system instability**. Use it in a **safe, isolated environment** (such as a virtual machine or sandbox) to avoid any negative impact on your main operating system.
- **Do not deploy zip bombs on public systems, websites, or services**.
- **Never use this code to harm or disrupt others**.
- Use this project solely to **understand the technical workings of zip bombs** and **how to prevent** them.

This project is licensed under the [MIT License](LICENSE).
Understanding how zip bombs work is important for cybersecurity professionals to recognize and defend against such attacks. This project is designed to help students, developers, and IT professionals learn more about file compression and security threats.

Please remember to act responsibly and consider the potential risks associated with the use of this code.
