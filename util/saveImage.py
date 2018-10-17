import requests;

def save_image(url, imageTitle):
    try:
        response = requests.get(url);
        if(200 == response.status_code):
            with open(imageTitle, "wb") as f:
                f.write(response.content);
    except requests.ConnectionError as e:
        print("fail download");