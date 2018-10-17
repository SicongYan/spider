import requests;
import os;
from hashlib import md5;
from urllib.parse import urlencode;
from multiprocessing.pool import Pool;

url = "https://www.toutiao.com/search_content/?";


def get_page(offset):
    params = {
        "offset": offset,
        "format": "json",
        "keyword": "美团",
        "autoload": "true",
        "count": "20",
        "cur_tab": "1"
    }
    target = url + urlencode(params);
    try:
        response = requests.get(target);
        if (200 == response.status_code):
            return response.json();
    except requests.ConnectionError as e:
        return None;


def parse_page(json):
    if (json):
        data = json["data"];
        for item in data:
            if("title" in item):
                title = item["title"];
                images = item["image_list"];
                for image in images:
                    yield {
                        "image": image["url"],
                        "title": title
                    }

def save_image(item):
    if not os.path.exists(item["title"]):
        os.mkdir(item["title"]);
    try:
        response = requests.get("http:" + item["image"]);
        if(200 == response.status_code):
            file_path = "{0}/{1}.{2}".format(item["title"], md5(response.content).hexdigest(), "jpg");
            if not os.path.exists(file_path):
                with open(file_path, "wb") as f:
                    f.write(response.content);
            else:
                print("already downloaded")
    except requests.ConnectionError as e:
        print("fail download")

def search_page(pageIndex):
    json = get_page(pageIndex);
    items = parse_page(json);
    for item in items:
        save_image(item);

GROUP_START = 0
GROUP_END = 7

if __name__ == '__main__':
    pool = Pool();
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)]);
    pool.map(search_page, groups);
    pool.close();
    pool.join();


