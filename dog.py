#!/usr/bin/env python
from urllib2 import *
def banner():
    print "\033[93m                               ___       ___\033[1;m"
    print "\033[93m                              |   \_____/   |\033[1;m"
    print "\033[93m                             /  |\/     \/|  \\    \033[1;m"
    print "\033[93m                             \_/ | /\ /\ | \_/\033[1;m"
    print "\033[97m ____  ____ _____ _____  __   _ \033[1;m \033[93m|_\/ \/_| \033[97m _____   ____   ____\033[1;m"
    print "\033[97m|___/  |___ |     |    | | \  | \033[1;m\033[93m/   \o/   \ \033[97m|    \ |    | | ___\033[1;m"
    print "\033[97m|   \_ |___ |____ |____| |  \_| \033[1;m\033[93m\___/'\___/ \033[97m|____/ |____| |____| v0.8\033[1;m"
    print "\t\t\033[97m     Made with \033[1;m\033[1;31m<3\033[1;31m\033[97m By Team Ultimate\033[1;m"
def menu():
    print "\n\033[97m1. Whois Lookup\033[1;m"
    print "\033[97m2. DNS Lookup + Cloudflare Detector\033[1;m"
    print "\033[97m3. Zone Transfer\033[1;m"
    print "\033[97m4. Port Scan\033[1;m"
    print "\033[97m5. HTTP Header Grabber\033[1;m"
    print "\033[97m6. Honeypot Detector\033[1;m"
    print "\033[97m7. Robots.txt Scanner\033[1;m"
    print "\033[97m8. Link Grabber\033[1;m"
    print "\033[97m9. IP Location Finder\033[1;m"
    print "\033[97m10. Traceroute\033[1;m"
def dog():
    try:
        choice = input('\033[1;91mEnter your choice:\033[1;m ')
        if choice == 1:
            domip = raw_input('\033[1;91mEnter Domain or IP Address: \033[1;m')
            who = "http://api.hackertarget.com/whois/?q=" + domip
            pwho = urlopen(who).read()
            print (pwho)
            menu()
            dog()
        if choice == 2:
            domain = raw_input('\033[1;91mEnter Domain: \033[1;m')
            ns = "http://api.hackertarget.com/dnslookup/?q=" + domain
            pns = urlopen(ns).read()
            print (pns)
            if 'cloudflare' in pns:
                print "\033[1;31mCloudflare Detected!\033[1;m"
            else:
                print "\033[1;31mNot Protected By cloudflare\033[1;m"
            menu()
            dog()
        if choice == 3:
            domain = raw_input('\033[1;91mEnter Domain: \033[1;m')
            zone = "http://api.hackertarget.com/zonetransfer/?q=" + domain
            try:
                domain = raw_input('\033[1;91mEnter Domain: \033[1;m')
                pzone = urlopen(zone).read()
                print (pzone)
            except 'failed' in pzone:
                print "\033[1;31mZone transfer failed\033[1;m"
            menu()
            dog()
        if choice == 4:
            domip = raw_input('\033[1;91mEnter Domain or IP Address: \033[1;m')
            port = "http://api.hackertarget.com/nmap/?q=" + domip
            pport = urlopen(port).read()
            print (pport)
            menu()
            dog()
        if choice == 5:
            domip = raw_input('\033[1;91mEnter Domain or IP Address: \033[1;m')
            header = "http://api.hackertarget.com/httpheaders/?q=" + domip
            pheader = urlopen(header).read()
            print (pheader)
            menu()
            dog()
        if choice == 6:
            ip = raw_input('\033[1;91mEnter IP Address: \033[1;m')
            honey = "https://api.shodan.io/labs/honeyscore/" + ip + "?key=C23OXE0bVMrul2YeqcL7zxb6jZ4pj2by"
            phoney = urlopen(honey).read()
            if '0.0' in phoney:
                print "\033[1;32mHoneypot Probabilty: 0%\033[1;m"
            if '0.1' in phoney:
                print "\033[1;32mHoneypot Probabilty: 10%\033[1;m"
            if '0.2' in phoney:
                print "\033[1;32mHoneypot Probabilty: 20%\033[1;m"
            if '0.3' in phoney:
                print "\033[1;32mHoneypot Probabilty: 30%\033[1;m"
            if '0.4' in phoney:
                print "\033[1;32mHoneypot Probabilty: 40%\033[1;m"
            if '0.5' in phoney:
                print "\033[1;31mHoneypot Probabilty: 50%\033[1;m"
            if '0.6' in phoney:
                print "\033[1;31mHoneypot Probabilty: 60%\033[1;m"
            if '0.7' in phoney:
                print "\033[1;31mHoneypot Probabilty: 70%\033[1;m"
            if '0.8' in phoney:
                print "\033[1;31mHoneypot Probabilty: 80%\033[1;m"
            if '0.9' in phoney:
                print "\033[1;31mHoneypot Probabilty: 90%\033[1;m"
            if '1.0' in phoney:
                print "\033[1;31mHoneypot Probabilty: 100%\033[1;m"
            menu()
            dog()
        if choice == 7:
            domain = raw_input('\033[1;91mEnter Domain: \033[1;m')
            if 'http://' in domain or 'https://' in domain:
                pass
            else:
                domain = 'http://' + domain
            robot = domain + "/robots.txt"
            probot = urlopen(robot).read()
            print (probot)
            menu()
            dog()
        if choice == 8:
            page = raw_input('\033[1;91mEnter URL: \033[1;m')
            if 'http://' in page or 'https://' in page:
                pass
            else:
                page = 'http://' + page
            crawl = "https://api.hackertarget.com/pagelinks/?q=" + page
            pcrawl = urlopen(crawl).read()
            print (pcrawl)
            menu()
            dog()
        if choice == 9:
            ip = raw_input('\033[1;91mEnter IP Address: \033[1;m')
            geo = "http://ipinfo.io/" + ip + "/geo"
            pgeo = urlopen(geo).read()
            print (pgeo)
            menu()
            dog()
        if choice == 10:
            domip = raw_input('\033[1;91mEnter Domain or IP Address: \033[1;m')
            trace = "https://api.hackertarget.com/mtr/?q=" + domip
            ptrace = urlopen(trace).read()
            print (ptrace)
            menu()
            dog()
        else:
            print "\033[1;31m[-] Invalid option!\033[1;m"
            menu()
            dog()
    except:
        print "\033[1;31m[-] Something went wrong!\033[1;m"
        menu()
        dog()
banner()
menu()
dog()
