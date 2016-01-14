import re

file = open(r'E:\大学课程相关\英语学习相关\voa英语\VOA慢速英语听力\VOA慢速英语听力2012年1—8月\2012年04月VOA慢速英语听力音频打包下载\15000-Websites-That-Spread-Terror-and-Hate.txt','r')

for line in file:
    object = re.match('^https?://',line)
    if object:
        print(line,end='')
    #print(line,end='')


str = input('enter a string:')
print(re.split('s',str))

