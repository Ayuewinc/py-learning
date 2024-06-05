import json
if __name__ == '__main__':
    mydict = {
        'name': 'Vic',
        'age': '33',
        'tel': '135444444444',
        'friend': 'Cheryl',
        'cars': [
            {'brand': 'BYD', 'max_speed': '120'},
            {'brand': 'Audi', 'max_speed': '180'},
            {'brand': 'Tesla', 'max_speed': '220'}
        ]
    }
    s = ""
    json_string = '{ "title": "Smartphone Market Share in China (May 2022)", "source": "Counterpoint Research", "data": [ { "model": "Apple iPhone 13", "market_share": 7 }, { "model": "Apple iPhone 13 Pro Max", "market_share": 6 }, { "model": "OPPO Reno 7 5G", "market_share": 5 } ] }'

    try:
        with open('data.json', 'w') as js:
            json.dump(mydict, js)
            json.dumps(mydict, s)
    except IOError as e:
        print(e)
    print("Save data completed!")

    resp = requests.get('http://api.tianapi.com/guonei/?key=0e714795391ae57c0fbc54ae39f1dd37&num=10')
    #data = json.loads(resp.text)
    """ for news in data['newslist']:
        print(news['title']) """
    data = json.loads(json_string)
    print(data)

