import requests;
from  pyquery import PyQuery as pq;

url = "https://www.zhihu.com/explore";
header = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
}


html = requests.get(url, headers = header).text;
print(html);
doc = pq(html);
items = doc(".explore-tab .feed-item").items();

file = open("explore.txt", "a", encoding="utf-8");
for item in items:
    question = item.find("h2").text();
    print(question);

    author = item.find(".author-link-line").text();
    content = pq(item.find(".content").html()).text();
    file.write("\n".join([question, author, content]));
    file.write("\n" + "=" * 50 + "\n");

file.close();
