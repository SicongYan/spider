import requests;
import re;
import os;

#爬取猫眼电影排行
target = "http://maoyan.com/board/4";
header = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
}

pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?<a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>上映时间：(.*?)</p>.*?integer.*?>(.*?)</i>.*?.fraction.*?>(.*?)</i>', re.S);

def get_one_page(url):
    response = requests.get(url, headers=header);
    if(200 == response.status_code):
        return response.text;

#写文件
def saveImg(imgUrl, imgName):
    response = requests.get(imgUrl);
    type = imgUrl.rfind(".");
    end = imgUrl.rfind("@");
    if(200 == response.status_code):
        with open("image/" + imgName + imgUrl[type:end], "wb") as file:
            file.write(response.content);

def getInfo(text):
    items = re.findall(pattern, text);
    for item in items:
        saveImg(item[1], item[0] + "." + item[2]);
        # yield {
        #     'index' : item[0],
        #     'image' : item[1],
        #     'title' : item[2],
        #     'actor' : item[3],
        #     'time' : item[4],
        #     'score' : item[5] + item[6]
        # }

if __name__ == '__main__':
    if not os.path.exists("./image"):
        os.mkdir("./image");
    for i in range(10):
      response = get_one_page(target +"?offset=" + str(i * 10));
      getInfo(response);