import requests;

if __name__ == '__main__':
    target = "http://gitbook.cn";
    res = requests.get(url=target);
    print(res.text);