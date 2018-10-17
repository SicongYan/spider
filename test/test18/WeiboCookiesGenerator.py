from test.test18.CookieGenerator import CookiesGenerator;
from test.test18.WeiboCookies import WeiboCookies;

class WeiboCookiesGenerator(CookiesGenerator):
    def __init__(self, website="weibo"):
        CookiesGenerator.__init__(self, website);
        self.website = website;

    def new_cookies(self, username, password):
        return WeiboCookies(username, password, self.browser).main();

if __name__ == '__main__':
    generator = WeiboCookiesGenerator();
    generator.run();