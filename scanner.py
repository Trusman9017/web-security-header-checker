import requests
import sys

def check_security_headers(url):
    """
    Простой сканер для проверки заголовков безопасности сайта.
    """
    # Добавляем http, если пользователь забыл
    if not url.startswith("http"):
        url = "https://" + url

    print(f"[*] Analyzing headers for: {url}\n")

    try:
        response = requests.get(url, timeout=5)
        headers = response.headers

        # Список важных заголовков безопасности
        security_headers = [
            "X-Frame-Options",           # Защита от Clickjacking
            "Content-Security-Policy",   # Защита от XSS
            "Strict-Transport-Security", # Принудительный HTTPS
            "X-Content-Type-Options",    # Защита от MIME-sniffing
            "Server"                     # (Инфо) Может выдать версию сервера
        ]

        for header in security_headers:
            if header in headers:
                print(f"[+] FOUND: {header}")
                # Для заголовка Server можно показать значение, чтобы знать версию ПО
                if header == "Server":
                    print(f"    Value: {headers[header]}")
            else:
                print(f"[-] MISSING: {header}")

    except requests.exceptions.RequestException as e:
        print(f"[!] Error connection to {url}: {e}")

if __name__ == "__main__":
    # Проверка, введен ли аргумент при запуске
    if len(sys.argv) < 2:
        print("Usage: python scanner.py <url>")
        print("Example: python scanner.py google.com")
    else:
        target_url = sys.argv[1]
        check_security_headers(target_url)
