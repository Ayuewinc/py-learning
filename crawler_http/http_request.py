import requests
import json

def get_filename(url):
    filename = url[url.rfind('/') + 1 : ]
    return filename

def download_pic(url):
    filename = get_filename(url)
    try:
        resp = requests.get(url)
        with open('./' + filename , 'wb') as f:
            f.write(resp.content)
    except:
        pass

if __name__ == '__main__': 
    url = 'https://apis.tianapi.com/petnews/index'
    params_list = {
        'key': '0e714795391ae57c0fbc54ae39f1dd37',
        'num': 5
    }

    resp = requests.get(url, params=params_list)
    data = resp.json()
 #   data = resp.content.decode()
    print(data)
 #   data = json.loads(resp.text)
 #   for relt in data['result']['newslist']:
 #       url = relt['picUrl']
 #       print('downloading:%s' % url)
 #       download_pic(url)
        

    
 #   resp = requests.get('http://api.tianapi.com/guonei/?key=0e714795391ae57c0fbc54ae39f1dd37&num=1')
 #   data = json.loads(resp.text)
 #   print(data)
 #   for news in data['newslist']:
 #       print(news['title'])
    
   