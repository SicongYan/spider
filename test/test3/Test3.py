from urllib import request;

#爬取行政区划

if __name__ == '__main__':
    target = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/index.html';

    header = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
    }

    req = request.Request(url=target, headers = header, method="GET")
    response = request.urlopen(req, timeout=2);
    print(response.status);
    print(response.getheaders());
    print(response.read().decode("gb2312"));
