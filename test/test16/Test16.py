from selenium import webdriver;
from selenium.common.exceptions import TimeoutException;
from selenium.webdriver.common.by import By;
from selenium.webdriver.support import expected_conditions as EC;
from selenium.webdriver.support.wait import WebDriverWait;
from urllib.parse import quote;
from pyquery import PyQuery as pq;

chrome_options = webdriver.ChromeOptions();
chrome_options.add_argument("--headless");
browser = webdriver.Chrome(chrome_options=chrome_options);
wait = WebDriverWait(browser, 10);
Key_word = "iphone X";
url = "https://s.taobao.com/search?q="

def index_page(page):
    try:
        browser.get(url + quote(Key_word));
        if(1 < page):
            input = wait.until(
                EC.presence_of_element_located(By.CSS_SELECTOR, "#spudetail-pager div.form > input")
            );
            submit = wait.until(
                EC.element_to_be_clickable(By.CSS_SELECTOR, "#spudetail-pager div.form > span.btn J_Submit")
            );
            input.clear();
            input.send_keys(page);
            submit.click()

        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#spudetail-pager li.item.active > span"), str(page))
        );
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.m-itemlist .items .item"))
        );
        get_products();
    except TimeoutException as e:
        index_page(page);

def get_products():
    html = browser.page_source;
    doc = pq(html);
    items = doc("#spudetail-itemlist .items .item").items();
    for item in items:
        print(item.find(".price").children("strong"));
        product = {
            "image" : item.find(".pic").attr("data-pic"),
            "price" : item.find(".price").text(),
            "deal" : item.find(".deal-cnt").text(),
            "title" : item.find(".title").text(),
            "shop" : item.find(".shop").text(),
            "location" : item.find(".location").text()
        }
        print(product);

if __name__ == '__main__':
    page = index_page(1);
    browser.close();
