import requests
import jsonpath
import pandas

url = 'https://www.sara.gov.cn/eportal/ui?portal.url=/portlet/place-info-front!queryList.portlet&moduleId=b68f71decbfb4ff4b274cac2bf67204b&pageId=614c812b4af64b4e91e31a7a7bc9f12a'
headers = {
  "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}
payload = {
    "currentPage": 1,
    "pageSize": 15
}

resp = requests.post(url, headers=headers, data=payload, verify=False)
data = resp.json()
# text = resp.json()
# print(text)
placeInfoId = []
religionName = []
faction = []
placeName = []
address = []
personCharge = []
province = []

placeInfoId = jsonpath.jsonpath(data, '$..placeInfoId')
religionName = jsonpath.jsonpath(data, '$..religionName')
faction = jsonpath.jsonpath(data, '$..faction')
placeName = jsonpath.jsonpath(data, '$..placeName')
address = jsonpath.jsonpath(data, '$..address')
personCharge = jsonpath.jsonpath(data, '$..personCharge')
province = jsonpath.jsonpath(data, '$..province')

table_data = [placeInfoId, religionName, faction, placeName, address, personCharge, province]
table_header = ['placeInfoId', 'religionName', 'faction', 'placeName', 'address', 'personCharge', 'province']
dataframe = pandas.DataFrame(dict(zip(table_header, table_data)))
dataframe.to_excel("./sara.xlsx", encoding='gbk', index=False)
