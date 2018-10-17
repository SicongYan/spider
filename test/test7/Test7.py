from urllib.robotparser import RobotFileParser;

rp = RobotFileParser("https://www.baidu.com/robots.txt");
rp.read();

print(rp.can_fetch("*", "https://www.baidu.com/baidu"));
print(rp.can_fetch("*", "https://image.baidu.com/s"));