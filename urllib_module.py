import urllib.request

web = urllib.request.urlopen('http://202.4.130.95')
file = open(r'H:\python\urlmodule_202.4.130.95.html','w')
print(web.getcode())
html = str(web.read())
file.write(html)
file.close()

print('done!')
print(web.read())
