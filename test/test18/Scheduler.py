import time;
from multiprocessing import Process;
from test.test18.RedisClient import RedisClient;
from test.test18.Api import app;
from test.test18.Config import *;
from test.test18.WeiboCookiesGenerator import *;
from test.test18.ValidTester import *;

class Scheduler(object):
    @staticmethod
    def valid_cookie(cycle=CYCLE):
        while True:
            print("Cookies检查start");
            try:
                for website, cls in TESTER_MAP.items():
                    tester = eval(cls + "(website='" + website + "')");
                    tester.run();
                    print("Cookies检测完成");
                    del tester;
                    time.sleep(cycle);
            except Exception as e:
                print(e.args);