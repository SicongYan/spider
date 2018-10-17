#登录github
import requests;
from lxml import etree;

class Login(object):
    def __init__(self):
        self.headers = {
            "Referer" : "https://github.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
            "Host" : "github.com"
        }
        self.login_url = "https://github.com/login";
        self.post_url = "https://github.com/session";
        self.logined_url = "https://github.com/settings/profile"
        self.session = requests.session();


    def get_token(self):
        response = self.session.get(self.login_url, headers = self.headers);
        selector = etree.HTML(response.text);
        token = selector.xpath("//div//input[2]/@value");
        return token;


    def login(self, email, password):
        post_data = {
            "commit" : "Sign in",
            "authenticity_token" : self.get_token(),
            "utf8" : "✓",
            "login" : email,
            "password" : password
        }

        response = self.session.post(self.post_url, data = post_data, headers = self.headers);
        if(200 == response.status_code):
            self.dynamics(response.text);
        response = self.session.get(self.login_url, headers = self.headers);
        if(200 == response.status_code):
            self.profile(response.text);

    def dynamics(self, html):
        selector = etree.HTML(html);
        dynamics = selector.xpath("//div[contains(@class, 'news')]//div[contains(@class, 'alert')]");
        for item in dynamics:
            dynamic = ' '.join(item.xpath(".//div[@class='title']//text()")).strip();
            print(dynamic);

    def profile(self, html):
        selector = etree.HTML(html);
        name = selector.xpath("//input[@id='user_profile_name']/@value")[0];
        email = selector.xpath("//select[@id='user_profile_email']/option[@value!='']/text()");
        print(name, email);

if __name__ == '__main__':
    login = Login();
    login.login(email="792800446@qq.com", password="****");
