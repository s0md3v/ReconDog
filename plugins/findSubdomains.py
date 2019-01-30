import sys
from re import findall
from requests import get

def findSubdomains(host):
    response = get('https://findsubdomains.com/subdomains-of/' +
                   host).text
    matches = findall(r'(?s)<div class="domains js-domain-name">(.*?)</div>', response)
    for match in matches:
        sys.stdout.write(match.replace(' ', '').replace('\n', '') + '\n')
