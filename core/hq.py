import re
import sys
import requests

from core.colors import bad, red, end

from plugins.whois import whois
from plugins.nsLookup import nsLookup
from plugins.findSubdomains import findSubdomains
from plugins.portScan import portScan
from plugins.detectTech import detectTech
from plugins.honeypot import honeypot
from plugins.detectCMS import detectCMS
from plugins.censys import censys
from plugins.reverseLookup import reverseLookup

database = {
    '1': [censys, 'ip'],
    '2': [nsLookup, 'domain'],
    '3': [portScan, 'domip'],
    '4': [detectCMS, 'domain'],
    '5': [whois, 'domip'],
    '6': [honeypot, 'ip'],
    '7': [findSubdomains, 'domain'],
    '8': [reverseLookup, 'ip'],
    '9': [detectTech, 'url']
}

if sys.version_info < (3, 0):
    input = raw_input


def getInput(typ):
    if typ == 'domip':
        typ = 'domain or ip'
    inp = input('%s%s>>%s  ' % (typ, red, end))
    return inp


def validate(inp, typ):
    if typ == 'ip':
        match = re.match(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', inp)
        if match:
            return inp
        else:
            return False
    elif typ == 'url':
        if inp.startswith('http'):
            return inp
        else:
            try:
                requests.get('https://' + inp)
                return 'https://' + inp
            except:
                return 'http://' + inp
    else:
        return inp


def hq(choice, target=False):
    if target:
        try:
            database[choice][0](target)
        except:
            print ('%s Skipped due to error: %s' % (bad, target))
    elif choice == '0':
        inp = getInput('all')
        for func in list(database.values()):
            try:
                func[0](inp)
                print (red + ('-' * 60) + end)
            except:
                pass
    elif not target:
        typ = database[choice][1]
        inp = getInput(typ)
        validatedInp = validate(inp, typ)
        if validatedInp:
            plugin = database[choice][0]
            plugin(validatedInp)
        else:
            print ('%s Invalid input type' % bad)
