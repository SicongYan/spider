import json;
from selenium import webdriver;
from selenium.webdriver import DesiredCapabilities;
from test.test18.Config import *;
from test.test18.RedisClient import RedisClient;

class CookiesGenerator(object):
    def __init__(self, website = "default"):
        """
        父类，初始化对象
        :param website:
        """
        self.website = website;
        self.cookies_db = RedisClient("cookies", self.website);
        self.accounts_db = RedisClient("accounts", self.website);
        self

    def init_brower(self):
        if("PhantomJS" == BROWSER_TYPE):
            caps = DesiredCapabilities.PHANTOMJS
            caps["phantomjs.page.settings.userAgent"] = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36";
            self.browser = webdriver.PhantomJS(desired_capabilities = caps);
            self.browser.set_window_size(1400, 500);
        elif("Chrome" == BROWSER_TYPE):
            self.browser = webdriver.Chrome();

    def new_cookies(self, username, password):
        raise NotImplementedError;

    def process_cookies(self, cookies):
        dict = {};
        for cookie in cookies:
            dict[cookie["name"]] = cookie["value"];
        return dict;

    def run(self):
        accounts_usernames = self.accounts_db.usernames();
        cookies_usernames = self.cookies_db.usernames();

        for username in accounts_usernames:
            if not username in cookies_usernames:
                password = self.accounts_db.get(username);
                print("正在生成Cookies", "账号", username, "密码", password);
                result = self.new_cookies(username, password);
                if 1 == result.get("status"):
                    cookies = self.process_cookies(result.get("content"));
                    print("成功保存cookies");

                elif 2 == result.get("status"):
                    print(result.get("content"));
                    if(self.accounts_db.delete(username)):
                        print("成功删除帐号");

                else:
                    print(result.get("content"));

    def close(self):
        try:
            print("Closing Brower");
            self.browser.close();
            del self.browser;
        except TypeError:
            print("Browser not open");
