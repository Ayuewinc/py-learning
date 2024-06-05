import requests
import json
import os
from concurrent.futures import ThreadPoolExecutor

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}

def download_pic(url):
    pic_name = url[url.rfind('/') + 1 :] 
    resp = requests.get(url, headers=headers)

    if resp.status_code == 200:
        with open(f'image/beauty/{pic_name}', 'wb') as f:
            f.write(resp.content)

def single_thread_download():
    for page in range(3):
        resp = requests.get(f'https://image.so.com/zjl?ch=beauty&sn={page * 30}') 
        if resp.status_code == 200:
            pic_dict_list = resp.json()['list']
            for pic_dict in pic_dict_list:
                download_pic(pic_dict['qhimg_url'])

def multi_thread_download():
    with ThreadPoolExecutor(max_workers=8) as pool:
        for page in range(3):
            resp = requests.get(f'https://image.so.com/zjl?ch=beauty&sn={page * 30}') 
            if resp.status_code == 200:
                pic_dict_list = resp.json()['list']
                for pic_dict in pic_dict_list:
                    pool.submit(download_pic, pic_dict['qhimg_url'])
    

if __name__ == '__main__':
    if not os.path.exists('./image/beauty'):
        os.makedirs('./image/beauty')
#    single_thread_download()
    multi_thread_download()

