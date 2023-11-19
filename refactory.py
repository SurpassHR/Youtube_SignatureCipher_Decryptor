import requests

if __name__ == '__main__':
    url = input("input youtube video url: ")
    url = "https://www.youtube.com/watch?v=mgO38dJ9NuU"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0",
    }
    req = requests.get(url=url, headers=headers)
    print(req.text)
