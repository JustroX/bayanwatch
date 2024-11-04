import os
from newsplease import NewsPlease
from dotenv import load_dotenv
load_dotenv()

proxy_url = os.getenv('PROXY_URL')
request_args = {
    "proxies": {
        "https": f"https://{proxy_url}",
        "http": f"http://{proxy_url}"
    }
}

for line in iter(input, ''):
    article = NewsPlease.from_url(line, request_args=request_args)
    print(article.get_serializable_dict())
