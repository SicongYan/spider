from urllib.error import URLError;
from urllib.request import ProxyHandler, build_opener;

target = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/index.html';
proxy_handler = ProxyHandler({
   "http" : "http://127.0.0.1:9723",
    "https" : "https://127.0.0.1:9723"
});

if __name__ == '__main__':
    opener = build_opener(proxy_handler);
    try:
        response  = opener.open(target);
        print(response.read().decode("gb2312"));
    except URLError as e:
        print(e.reason);