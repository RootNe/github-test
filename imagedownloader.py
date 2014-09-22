import re
import os

try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen

urlpattern = r'\"(?:http://)?[a-zA-Z0-9\/\(\)\-\_\\\s]+\.(?:jpe?g|png|gif)\"'
namepattern = r'(?:\/)[a-zA-Z0-9\(\)\-\_\.\\\s]+\.(?:jpe?g|png|gif)'
keepname = False
filenum = 0

url = raw_input('URL : ')
if url[:7] != 'http://' and url[8:] != 'https://':
    url = 'http://' + url
if url[-1] is not '/':
    url = url + '/'
filenum = 0

folder = raw_input('Directory : ')
if folder[-2:] == '/k':
    keepname = True
    folder = folder[:-2]
folder = './' + folder + '/'

d = os.path.dirname(folder)
if not os.path.exists(d):
    os.makedirs(d)

source = str(urlopen(url).read())

link = re.findall(urlpattern, source)


print(source)
print('\n\n\n\n')
for img in link:
    if keepname:
        filename = folder + re.findall(namepattern, img)[0][1:]
    else:
        filename = folder + 'img' + str(filenum) + '.' + img[-4:-1]

    if img[:8] == '"http://':
        img = img[1:-1]
    else:
        img = url+img[1:-1]

    print (img)
    f = urlopen(img)
    with open(filename, 'wb') as code:
        code.write(f.read())
    filenum += 1

print('\n\n')
print('%d files' % filenum)
print('Keep Name : ' + str(keepname))
