import sys
from re import findall
from tld import get_tld
from requests import get

def findSubdomains(host):
    response = get('https://findsubdomains.com/subdomains-of/' +
                   get_tld(host, fix_protocol=True)).text
    matches = findall(r'(?s)<div class="domains js-domain-name">(.*?)</div>', response)
    for match in matches:
        sys.stdout.write(match.replace(' ', '').replace('\n', '') + '\n')
