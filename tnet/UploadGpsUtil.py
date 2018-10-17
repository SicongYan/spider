import requests;
import sys;
import time;
import json;

url = "http://gps-rulai-dev1.800best.com/t8/location/accept";
header = {
    "Content-Type" : "application/json",
    "appName" : "TNET",
    "reporter" : "god",
    "token" : "7baffe1ae0ed4228bc0ed548afaae082",
}

def postData2Gps(driverId, toCode, longitude, latitude, createTime):
    header["driverId"] = driverId;
    header["shipmentCode"] = toCode;
    data = json.dumps([createPo(longitude, latitude, createTime)]);
    print(requests.post(url, headers=header, data=data));
    print("success");

def createPo(longitude=120, latitude=30, createTime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())):
    return {
        "longitude" : longitude,
        "latitude" : latitude,
        "createTime" : createTime,
        "reporter" : "god"
    };

if __name__ == '__main__':
    driverId = sys.argv[1];
    toCode = sys.argv[2];
    longitude = sys.argv[3];
    latitude = sys.argv[4];
    createTime = sys.argv[5];
    postData2Gps(driverId, toCode, longitude, latitude, createTime);


