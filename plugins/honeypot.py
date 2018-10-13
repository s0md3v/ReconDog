import sys
from requests import get
from core.colors import bad, info, red, green, end


def honeypot(inp):
    honey = 'https://api.shodan.io/labs/honeyscore/%s?key=C23OXE0bVMrul2YeqcL7zxb6jZ4pj2by' % inp
    try:
        result = get(honey).text
    except:
        result = None
        sys.stdout.write('%s No information available' % bad + '\n')
    if result:
        if float(result) < 0.5:
            color = green
        else:
            color = red
        probability = str(float(result) * 10)
        sys.stdout.write('%s Honeypot Probabilty: %s%s%%%s' %
                         (info, color, probability, end) + '\n')
