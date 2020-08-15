from bs4 import BeautifulSoup
import urllib

url = 'https://www.random.org/integers/?num=100&min=1&max=100&col=5&base=10&format=plain&rnd=new'

html = urllib.request.urlopen(url).read()

parsed_html = BeautifulSoup(html, features="lxml")

print(html)
