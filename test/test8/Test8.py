import requests;
import re;

header = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
}

r = requests.get("https://www.zhihu.com/explore", headers = header);
print(r.text);

pattern = re.compile("explore-feed.*?question_link.*?>(.*?)</a>", re.S);
titles = re.findall(pattern, r.text);
print(titles);