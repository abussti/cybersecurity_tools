🔍 Python Port Scanner

A simple Python-based port scanner that checks all ports (1–65535) on a target host and reports which ones are open.
This tool is ideal for learning about networking, sockets, and basic cybersecurity scanning techniques.

✨ Features

Scans all ports on a target IP

Uses Python’s built-in socket library

Displays each open port in real time

Includes exception handling (invalid host, connection issues, user cancellation)

Shows total scan time

🧠 How It Works

The user enters a domain or IP.

Python resolves the hostname to an IP address.

The script tries connecting to each port sequentially using socket.connect_ex().

Open ports are displayed on screen.

The scan duration is calculated and printed.

🚀 How to Run

Make sure you have Python installed.

Run the script:

python3 port_scanner.py


Enter the target hostname or IP when prompted:

Enter a remote host to scan: scanme.nmap.org

📘 Example Output
------------------------------------------------------------
Please wait, scanning remote host 45.33.32.156
------------------------------------------------------------
Port 22: Open
Port 80: Open
Port 9929: Open
Port 31337: Open
Scanning completed in:  0:00:32.814920

🛡️ Disclaimer

This tool is intended only for educational and authorized testing purposes.
Do not scan systems you do not own or do not have permission to test.

🎓 Author

Ahmad Bussti
Cybersecurity Student — Euclea Business School (Graduating 2027)
