import os
from newsplease import NewsPlease

directory_path = 'files/htmls'

for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            html = file.read()
            article = NewsPlease.from_html(html)
            print(article.get_serializable_dict())
