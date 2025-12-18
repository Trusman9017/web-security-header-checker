# Simple Web Security Header Scanner

A simple Python automation script designed to check a target website for missing HTTP security headers. 
This tool helps identify basic security misconfigurations related to OWASP recommendations.

### Features
Checks for the presence of:
- `X-Frame-Options` (Clickjacking protection)
- `Content-Security-Policy` (XSS protection)
- `Strict-Transport-Security` (HSTS)
- `X-Content-Type-Options`

### Usage
1. Clone the repository
2. Run the script:
   ```bash
   python scanner.py example.com
