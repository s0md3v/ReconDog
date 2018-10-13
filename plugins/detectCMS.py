import sys
from re import search
from requests import get
from core.colors import info, good


def detectCMS(domain):
    response = get('https://whatcms.org/?s=%s' % domain).text
    match = search(r'<a href="/c/\w+" class="nowrap" title="\w+">(.*?)</a></div>', response)
    try:
        sys.stdout.write(good + ' ' + match.group(1).split('</a>')[0] + '\n')
    except:
        sys.stdout.write('%s Target doesn\'t seem to use a CMS' % info + '\n')
