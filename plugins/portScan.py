import sys
from requests import get


def portScan(inp):
    result = get('http://api.hackertarget.com/nmap/?q=' + inp).text
    sys.stdout.write(result)
