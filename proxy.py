import requests

def check_proxy(proxy_url):
    url = 'https://2ip.ua/ru/'
    proxies = {'http': proxy_url, 'https': proxy_url}

    try:
        response = requests.get(url, proxies=proxies, timeout=10000)
        print(response)
        if response.status_code == 200:
            print("Proxi is work")
        else:
            print("Behind a proxy")
    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    proxy_url = 'http://117.250.3.58:8080'
    check_proxy(proxy_url)
