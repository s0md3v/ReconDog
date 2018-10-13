import sys
from requests import get
from core.colors import bad


def reverseLookup(inp):
    lookup = 'https://api.hackertarget.com/reverseiplookup/?q=%s' % inp
    try:
        result = get(lookup).text
        sys.stdout.write(result)
    except:
        sys.stdout.write('%s Invalid IP address' % bad)
