from bs4 import BeautifulSoup
import urllib

# Need to generate numbers in a single column

url = 'https://www.random.org/integers/?num=100&min=1&max=100&col=1&base=10&format=plain&rnd=new'

html = urllib.request.urlopen(url).read()

parsed_html = BeautifulSoup(html, features="html.parser")

print(parsed_html)

nums = list(parsed_html)

print(nums)

'''
nums = list(map(int, list(parsed_html.split())))

print(nums)
'''
