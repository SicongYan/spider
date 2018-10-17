import urllib.request;
import socket;
import urllib.error;

if __name__ == '__main__':
    target = 'https://www.python.org';

    try:
        response = urllib.request.urlopen(target, timeout=0.1);
        print(response.status);
        print(response.getheaders());
        print(response.read().decode('UTF-8'));
    except urllib.error.URLError as e:
        if isinstance(e.reason,  socket.timeout):
            print("time out");
