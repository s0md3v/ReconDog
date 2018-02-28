#!/usr/bin/env python
import sys

VER = 2

try:
    if sys.version_info >= (3,0):
        VER = 3
        from urllib.request import urlopen
        from urllib.error import URLError
    else:
        input = raw_input
        from urllib2 import urlopen
        from urllib2 import URLError
except:
        pass


def fetch(url, decoding='utf-8'):
    "Fetches content of URL"
    return urlopen(url).read().decode(decoding)

def banner():
    print("\033[93m                               ___       ___\033[1;m")
    print("\033[93m                              |   \_____/   |\033[1;m")
    print("\033[93m                             /  |\/     \/|  \\    \033[1;m")
    print("\033[93m                             \_/ | /\ /\ | \_/\033[1;m")
    print("\033[97m ____  ____ _____ _____  __   _ \033[1;m \033[93m|_\/ \/_| \033[97m _____   ____   ____\033[1;m")
    print("\033[97m|___/  |___ |     |    | | \  | \033[1;m\033[93m/   \o/   \ \033[97m|    \ |    | | ___\033[1;m")
    print("\033[97m|   \_ |___ |____ |____| |  \_| \033[1;m\033[93m\___/'\___/ \033[97m|____/ |____| |____| v0.8\033[1;m")
    print("\t\t\033[97m     Made with \033[1;m\033[1;31m<3\033[1;31m\033[97m By Team Ultimate\033[1;m")

def menu():
    print("\n\033[97m1. Whois Lookup\033[1;m")
    print("\033[97m2. DNS Lookup + Cloudflare Detector\033[1;m")
    print("\033[97m3. Zone Transfer\033[1;m")
    print("\033[97m4. Port Scan\033[1;m")
    print("\033[97m5. HTTP Header Grabber\033[1;m")
    print("\033[97m6. Honeypot Detector\033[1;m")
    print("\033[97m7. Robots.txt Scanner\033[1;m")
    print("\033[97m8. Link Grabber\033[1;m")
    print("\033[97m9. IP Location Finder\033[1;m")
    print("\033[97m10. Traceroute\033[1;m")
    print("\033[97m11. Exit\033[1;m")

def dog():
    choice = '1'         # Set as default to enter in the loop
    banner()

    while choice != '11':
        menu()
        choice = input('\033[1;91mEnter your choice:\033[1;m ')

        if choice == '1':
            domip = input('\033[1;91mEnter Domain or IP Address: \033[1;m')
            who = "http://api.hackertarget.com/whois/?q=" + domip
            pwho = fetch(who)
            print(pwho)

        elif choice == '2':
            domain = input('\033[1;91mEnter Domain: \033[1;m')
            ns = "http://api.hackertarget.com/dnslookup/?q=" + domain
            pns = fetch(ns)
            print(pns)

            if 'cloudflare' in pns:
                print("\033[1;31mCloudflare Detected!\033[1;m")
            else:
                print("\033[1;31mNot Protected By cloudflare\033[1;m")

        elif choice == '3':
            domain = input('\033[1;91mEnter Domain: \033[1;m')
            zone = "http://api.hackertarget.com/zonetransfer/?q=" + domain
            pzone = fetch(zone)
            print(pzone)
            if 'failed' in pzone:
                print("\033[1;31mZone transfer failed\033[1;m")

        elif choice == '4':
            domip = input('\033[1;91mEnter Domain or IP Address: \033[1;m')
            port = "http://api.hackertarget.com/nmap/?q=" + domip
            pport = fetch(port)
            print (pport)

        elif choice == '5':
            domip = input('\033[1;91mEnter Domain or IP Address: \033[1;m')
            header = "http://api.hackertarget.com/httpheaders/?q=" + domip
            pheader = fetch(header)
            print(pheader)

        elif choice == '6':
            ip = input('\033[1;91mEnter IP Address: \033[1;m')
            honey = "https://api.shodan.io/labs/honeyscore/" + ip + "?key=C23OXE0bVMrul2YeqcL7zxb6jZ4pj2by"
            
            try:
                phoney = fetch(honey)
            except URLError:
                phoney = None
                print('\033[1;31m[-] No information available for that IP!\033[1;m')
            
            if phoney:
                print('\033[1;3{color}mHoneypot Probabilty: {probability}%\033[1;m'.format(color='2' if float(phoney) < 0.5 else '3', probability=float(phoney) * 10))
 

        elif choice == '7':
            domain = input('\033[1;91mEnter Domain: \033[1;m')

            if not (domain.startswith('http://') or domain.startswith('https://')):
                domain = 'http://' + domain
            robot = domain + "/robots.txt"
            
            try:
                probot = fetch(robot)
                print(probot)
            except URLError:
                print('\033[1;31m[-] Can\'t access to {page}!\033[1;m'.format(page=robot))        

        elif choice == '8':
            page = input('\033[1;91mEnter URL: \033[1;m')

            if not (page.startswith('http://') or page.startswith('https://')):
                page = 'http://' + page
            crawl = "https://api.hackertarget.com/pagelinks/?q=" + page
            pcrawl = fetch(crawl)
            print (pcrawl)

        elif choice == '9':
            ip = input('\033[1;91mEnter IP Address: \033[1;m')
            geo = "http://ipinfo.io/" + ip + "/geo"
            
            try:
                pgeo = fetch(geo)
                print(pgeo)
            except URLError:
                print('\033[1;31m[-] Please provide a valid IP address!\033[1;m')

        elif choice == '10':
            domip = input('\033[1;91mEnter Domain or IP Address: \033[1;m')
            trace = "https://api.hackertarget.com/mtr/?q=" + domip
            ptrace = fetch(trace)
            print (ptrace)

        elif choice == '11':
            print('\033[97m11. Exiting\033[1;m')

        else:
            print('\033[1;31m[-] Invalid option!\033[1;m')
        #except:
        #    print('\033[1;31m[-] Something wrong happened!\033[1;m')


#=====# Main #=====#

if __name__ == '__main__':
    dog()
