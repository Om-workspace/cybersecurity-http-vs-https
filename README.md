🔐 HTTP vs HTTPS Security Demonstration with Payment Tampering & SQL Injection

This project demonstrates the security risks of HTTP-based websites and how HTTPS with SSL protects against cyber attacks.
A course-selling website is developed where attackers can tamper cart values, intercept payment data, and perform SQL Injection in the insecure version, while the HTTPS version prevents these attacks.

🎯 Objectives
Demonstrate HTTP vulnerability
Show Man-in-the-Middle (MITM) attack
Demonstrate cart value tampering
Demonstrate payment information leakage
Demonstrate SQL Injection login bypass
Implement HTTPS using SSL certificate
Show secure encrypted communication

🧪 Attack Scenarios Demonstrated

1. Cart Price Tampering (HTTP)

Attacker modifies total amount before payment

Example:

Actual Total = ₹4598
Tampered Total = ₹10

Server accepts modified value in HTTP version.

2. Payment Information Leakage (HTTP)

Attacker intercepts:

Card Number
CVV
Name
Amount

Data transmitted in plain text over HTTP.

3. SQL Injection Attack

Login bypass using:

username: admin
password: ' OR '1'='1

This allows attacker unauthorized access.

4. HTTPS Protection

After enabling HTTPS with SSL:

Data encrypted using TLS
Cart tampering prevented
Payment details secured
MITM attack fails
Secure authentication

🏗 Project Structure

http-vs-https-security-demo
│
├── http-insecure
│   ├── app.py
│   ├── users.db
│   └── templates
│       ├── index.html
│       └── attack.html
│
├── https-secure
│   ├── app.py
│   ├── users.db
│   ├── cert.pem
│   ├── key.pem
│   └── templates
│       ├── index.html
│       └── attack.html
│
└── README.md
🛒 Courses Available (Demo Store)

The website includes 10 courses:

Python for Beginners
Ethical Hacking Basics
Data Science Bootcamp
Web Development Full Stack
Machine Learning A-Z
Cyber Security Fundamentals
Docker & Kubernetes
Java Masterclass
React Complete Guide
SQL Injection Mastery

Users can add courses to cart and proceed to payment.

🚨 HTTP Version (Insecure)

Vulnerabilities:

No encryption
Cart price can be modified
Payment data exposed
SQL injection possible
MITM attack successful

URL example:

http://localhost:5000
🔐 HTTPS Version (Secure)

Security features:

SSL certificate
TLS encryption
Secure payment transmission
Data integrity protection
Attack detection page

URL example:

https://localhost:5000
⚙️ Installation

Clone repository:

git clone https://github.com/yourusername/http-vs-https-security-demo.git
▶ Run HTTP Version
cd http-insecure
pip install flask
python app.py

Open:

http://localhost:5000
▶ Run HTTPS Version

Generate SSL certificate:

openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes

Run:

cd https-secure
python app.py

Open:

https://localhost:5000
🧠 Technologies Used
Python Flask
SQLite Database
HTML/CSS
OpenSSL
HTTP Protocol
HTTPS / TLS
SQL Injection
MITM Attack Simulation

📊 Demonstration Flow

HTTP Demo
Select courses
Add to cart
Modify total amount
Payment processed
Attack successful
HTTPS Demo
Select courses
Add to cart
Attempt tampering
Request encrypted
Attack blocked

✅ Conclusion

The project demonstrates that HTTP websites are vulnerable to attacks such as cart tampering, SQL injection, and payment data interception. After implementing HTTPS using SSL certificates, all communications are encrypted and attacks are prevented. This proves that HTTPS ensures confidentiality, integrity, and authentication.