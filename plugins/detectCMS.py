import sys
from re import search
from requests import get
from core.colors import info, good


def detectCMS(domain):
    response = get('https://whatcms.org/?gpreq=json&jsoncallback=jQuery1124008091494457806547_1554361369057&s=%s&na=&nb=1cg805dlm7d7e5eickf67rzxrn12mju6bnch3a99hrt88v7n8rhf0lovwr8d0zm1&verified=&_=1554361369059' % domain).text
    match = search(r'uses<\\/div>[^>]+>(.*?)<\\/a>', response)
    try:
        sys.stdout.write(good + ' ' + match.group(1) + '\n')
    except:
        sys.stdout.write('%s Target doesn\'t seem to use a CMS' % info + '\n')
