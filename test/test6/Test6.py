from urllib.parse import urlparse, urlunsplit, quote, unquote;

result = urlparse("https://www.baidu.com/index.html;user?id=5#comment", allow_fragments=True);
print(result);

print(urlunsplit(["1", "2", "3", "4", "5"]));

print(quote("就是"));
print(unquote("%E5%B0%B1%E6%98%AF"));