from selenium import webdriver;
from selenium.common.exceptions import TimeoutException;
from selenium.webdriver.common.by import By;
from selenium.webdriver.support.ui import WebDriverWait;
from selenium.webdriver.support import expected_conditions as EC;
from scrapy.http import HtmlResponse;
from logging import getLogger;

class SeleniumMiddleware():
    def __init__(self, timeout=None, service_args=[]):
        self.logger = getLogger(__name__);
        self.timeout = timeout;
        self.browser = webdriver.PhantomJS(service_args = service_args);
        self.browser.set_window_size(1400, 700);
        self.browser.set_page_load_timeout(self.timeout);
        self.wait = WebDriverWait(self.browser, self.timeout);

    def __del__(self):
        self.browser.close();

    def process_request(self, request, spider):
        self.logger.debug("PhantomJS is starting");
        page = request.meta.get("page", 1);
        try:
            self.browser.get(request.url);
            if 1 < page:
                input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager div.form > input")));
                submit = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#mainsrp-pager div.form > span.btn.J_Submit")));
                input.clear();
                input.send_keys(page);
                submit.click();
                return HtmlResponse(url=request.url, body=self.browser.page_source, request=request, encoding="utf-8", status=200);
        except TimeoutException:
            return HtmlResponse(url=request.url, status=500, request=request);

    @classmethod
    def from_crawler(cls, crwaler):
        return cls(timeout=crwaler.settings.get("SELENIUM_TIMEOUT"), service_args=crwaler.settings.get("PHANTOMJS_SERVICE_ARGS"));