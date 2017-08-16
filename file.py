from urllib import request

f = open("./test.txt", "w")
f.write("test")
f.close()

response = request.urlopen("http://www.baidu.com")
f = open("baidu.txt","w")
page = f.write(str(response.read()))
f.close()