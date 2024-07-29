import requests
url = "https://github.com/HOMENYK/Redactor-python-"
Git_code = requests.get(url).content
F1 = open("Main.exe", "w+", encoding='utf-8')
F1.write(Git_code)
F1.close()
