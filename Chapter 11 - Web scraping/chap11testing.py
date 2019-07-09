import webbrowser,requests, bs4
#webbrowser.open('http://inventwithpython.com/')
#res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
#print(type(res))
#print(res.status_code == requests.codes.ok)
#print(len(res.text))
#print(res.text[:250])
# res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
# try:
#    res.raise_for_status()
# except Exception as exc:
#     print('There was a problem: %s' % (exc))

# Always call raise_for_status() after calling requests.get().
# You want to be sure that the download has actually worked before your program continues.

#res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
#res.raise_for_status()
#playFile = open('RomeoAndJuliet.txt', 'wb')
#for chunk in res.iter_content(100000):
#        playFile.write(chunk)
#playFile.close()

res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text,"html.parser")
print(type(noStarchSoup))
elems = noStarchSoup.select('#author')
print(type(elems))
print(len(elems))
print(type(elems[0]))
print(elems[0].getText())
print(str(elems[0]))
print(elems[0].attrs)

# BeautifulSoup 4
# Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

