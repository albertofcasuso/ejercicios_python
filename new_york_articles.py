import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/es/"
r = requests.get(url)
r_html = r.content

r_html = BeautifulSoup(r_html, 'html.parser')
for articulos in r_html.find_all(class_="css-l2vidh"):
    if articulos.a.contents:
        titulo = str(articulos.a.contents)
        print (titulo)
