# 🔐 SSL Certificate Checker (Python)

A simple Python script to fetch and display SSL certificate details of a given hostname.

---

## 🚀 Features

* Retrieves SSL certificate from a remote server
* Displays:

  * Issuer (Organization)
  * Expiry Date
  * Days remaining
  * Certificate status (Valid / Expired)

---

## 🛠️ Requirements

* Python 3.x
* No external libraries required (uses built-in modules)

---

## 📦 Modules Used

* `ssl`
* `socket`
* `datetime`

---

## ▶️ Usage

```bash
python ssl_checker.py
```

Then enter the hostname:

```bash
Enter the hostname (e.g., www.example.com): google.com
```

---

## 📊 Sample Output

```
SSL Certificate Information for google.com

Issuer: Google Trust Services
Expiry Date: Jun 10 12:00:00 2026 GMT
Days Left: 70
Status: Valid
```

---

## ⚙️ How It Works

* Establishes a TCP connection to port 443
* Wraps the socket with SSL
* Retrieves certificate using `getpeercert()`
* Parses expiry date and calculates remaining days

---

## ⚠️ Notes

* Works only for HTTPS-enabled domains (port 443)
* Requires internet connection
* Time is calculated based on local system clock

---
