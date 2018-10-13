import re


def extractor(inpList, kind):
    parsed = set()
    inp = ''.join(inpList)
    domain = r'[\w\.\-]+'
    ip = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
    if kind == 'domain':
        pattern = domain
    else:
        pattern = ip
    matches = re.findall(pattern, inp)
    for match in matches:
        if kind == 'ip':
            parsed.add(match)
        else:
            if not re.match(ip, match):
                parsed.add(match)
    return parsed
