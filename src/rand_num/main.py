from bs4 import BeautifulSoup
import urllib

# Need to generate numbers in a single column
url = 'https://www.random.org/integers/?num=100&min=1&max=100&col=1&base=10&format=plain&rnd=new'
html = urllib.request.urlopen(url).read()

parsed_html = BeautifulSoup(html, features="html.parser")
print(parsed_html)

# nums = list(map(int, parsed_html.string.split('\n')))
list1 = parsed_html.string.split('\n')
print(list1)

del list1[-1]
print(list1)

nums = list(map(int, list1))
print(nums)
