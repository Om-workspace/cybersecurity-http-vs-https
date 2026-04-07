# HTTP vs HTTPS Security Demonstration

Payment Tampering • SQL Injection • MITM • Docker • Ansible

## Overview

This project demonstrates the security risks of HTTP-based websites and how HTTPS with SSL/TLS protects against cyber attacks.
A course-selling platform is developed where attackers can tamper cart values, intercept payment data, and perform SQL injection in the insecure version, while the HTTPS version prevents these attacks. Both applications are containerized using Docker and deployed using Ansible.

## Objectives

* Demonstrate insecure HTTP communication
* Show cart price tampering attack
* Demonstrate payment data leakage
* Demonstrate SQL injection login bypass
* Simulate Man-in-the-Middle (MITM) attack
* Implement HTTPS using SSL certificate
* Secure transactions using TLS encryption
* Containerize applications using Docker
* Automate deployment using Ansible

## Attack Scenarios Demonstrated

### 1. Cart Value Tampering (HTTP)

Attacker modifies total cart value before payment
Example:
Actual Total = ₹4598
Tampered Total = ₹10
Server accepts modified value in HTTP version.

### 2. Payment Data Leakage (HTTP)

Sensitive information transmitted in plain text:

* Card number
* CVV
* User name
* Amount

Attacker can intercept this data.

### 3. SQL Injection Attack

Login bypass using:
username: admin
password: ' OR '1'='1

This allows unauthorized access.

### 4. MITM Attack

Attacker intercepts HTTP request and modifies:
amount=4598 → amount=1
Transaction manipulated successfully.

### 5. HTTPS Protection

After enabling HTTPS:

* Data encrypted
* Cart tampering prevented
* Payment secured
* MITM blocked
* Credentials protected

## Demo Course Store

The application simulates an online course marketplace with 10 courses:

* Python for Beginners
* Ethical Hacking Basics
* Data Science Bootcamp
* Web Development Full Stack
* Machine Learning A-Z
* Cyber Security Fundamentals
* Docker & Kubernetes
* Java Masterclass
* React Complete Guide
* SQL Injection Mastery

Users can select courses, generate cart total, and proceed to payment.

## Project Structure

http-vs-https-security-demo
│
├── http-insecure
│   ├── app.py
│   ├── users.db
│   ├── Dockerfile
│   └── templates
│       ├── index.html
│       └── attack.html
│
├── https-secure
│   ├── app.py
│   ├── users.db
│   ├── cert.pem
│   ├── key.pem
│   ├── Dockerfile
│   └── templates
│       ├── index.html
│       └── attack.html
│
└── ansible
    ├── inventory.ini
    └── deploy.yml
    
## Docker Deployment

Build HTTP image:
docker build -t http-insecure ./http-insecure

Build HTTPS image:
docker build -t https-secure ./https-secure

Run HTTP container:
docker run -d -p 5000:5000 http-insecure

Run HTTPS container:
docker run -d -p 5443:5000 https-secure

## Ansible Deployment

Run automated deployment:
ansible-playbook -i ansible/inventory.ini ansible/deploy.yml

This playbook:

* Builds docker images
* Runs containers
* Exposes ports
* Deploys both environments

## Access Applications

HTTP (Insecure)
http://localhost:5000

HTTPS (Secure)
https://localhost:5443

## Security Comparison

Feature | HTTP | HTTPS
Data Encryption | No | Yes
Cart Tampering | Possible | Blocked
SQL Injection | Possible | Prevented
Payment Leakage | Yes | Encrypted
MITM Attack | Successful | Failed
SSL Certificate | No | Yes

## Technologies Used

* Python Flask
* SQLite Database
* HTML/CSS
* OpenSSL
* HTTP / HTTPS
* TLS Encryption
* SQL Injection
* Docker
* Ansible

## Demonstration Flow

HTTP Demo

1. Login using SQL injection
2. Select courses
3. Generate cart value
4. Tamper total amount
5. Payment processed
6. Attack successful

HTTPS Demo

1. Login securely
2. Select courses
3. Attempt tampering
4. TLS encryption applied
5. Attack blocked
6. Secure payment

## Learning Outcomes

* Difference between HTTP and HTTPS
* SSL/TLS implementation
* Payment tampering attacks
* SQL injection vulnerability
* MITM attack simulation
* Docker container deployment
* Ansible automation
* Secure web application design

## Mini Project Type

Cyber Security Mini Project
HTTP vs HTTPS Security Demonstration
Payment Gateway Tampering Simulation
Docker & Ansible Deployment

* pip install --user ansible
* pip install --user docker
* ansible-playbook -i ansible/inventory.ini deploy.yml
