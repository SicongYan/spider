from urllib.parse import urlencode;
from pyquery import PyQuery as pq;
import requests;

baseUrl = "https://m.weibo.cn/api/container/getIndex?";
header = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
}

def get_page(page):
    params = {
        "type" : "uid",
        "value" : "2830678474",
        "containerid" : "1076032830678474",
        "page" : page
    }
    url = baseUrl + urlencode(params);
    try:
        response = requests.get(url, headers=header);
        if(200 == response.status_code):
            return response.json();
    except requests.ConnectionError as e:
        print("Error", e.args);

def parse_page(json):
    if(json):
        items = json["data"]["cards"];
        for item in items:
            if("mblog" in item):
                mblog = item["mblog"];
                weibo = {};
                weibo["id"] = mblog["id"];
                weibo["text"] = pq(mblog["text"]).text();
                yield weibo;

if __name__ == '__main__':
    for pageIndex in range(10):
        page = get_page(pageIndex);
        results = parse_page(page);
        for result in results:
            print(result);