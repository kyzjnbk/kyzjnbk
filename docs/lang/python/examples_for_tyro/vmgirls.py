# %%
'''
A simple example of spider
'''

import requests
import re
import os
import time
# from headers import get_headers

# %%
def askURL(url):
    head = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
    }
    response = requests.get(url, headers = head)
    html = response.text

    return html

def main():
    #baseurl = 'https://www.vmgirls.com/13344.html'
    #baseurl = 'https://www.vmgirls.com/16121.html'
    baseurl = 'https://www.vmgirls.com/17103.html'
    html = askURL(baseurl)

    urls = re.findall('<a href="(.*?)" alt=".*?" title=".*?">', html)
    dir_name = re.findall('<a href=".*?" alt=".*?" title="(.*?)">', html)[0]

    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

    for url in urls:
        time.sleep(1)
        print(url)
        file_name = url.split('/')[-1]
        head = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
        }
        response = requests.get('https:' + url, headers = head)
        with open(dir_name + '/' + file_name, 'wb') as f:
            f.write(response.content)

# %%
if __name__ == '__main__': 
    main()
    print('爬取完毕')

# %%
