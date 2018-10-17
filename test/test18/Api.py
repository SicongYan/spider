import json;
from flask import Flask, g;

app = Flask(__name__);

GENERATOR_MAP = {
    "weibo" : "WeiboCookiesGenerator"
}
@app.route("/")
def index():
    return "<h2>welcome</h2>";

def get_con():
    for website in GENERATOR_MAP:
        if not hasattr(g, website):
            setattr(g, website + "_cookies", eval("RedisClient" + "('cookies', '" + website + "')"));
        return g;

@app.route("/<website>/random")
def random(website):
    """
    获取随机的cookie
    :param website:
    :return:
    """
    g = get_con();
    cookies = getattr(g, website + "_cookies").random();
    return cookies;