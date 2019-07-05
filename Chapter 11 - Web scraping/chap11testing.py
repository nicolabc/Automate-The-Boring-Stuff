import webbrowser,requests
#webbrowser.open('http://inventwithpython.com/')
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(type(res))
print(res.status_code == requests.codes.ok)
print(len(res.text))
print(res.text[:250])
# res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
# try:
#    res.raise_for_status()
# except Exception as exc:
#     print('There was a problem: %s' % (exc))

# Always call raise_for_status() after calling requests.get().
# You want to be sure that the download has actually worked before your program continues.

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
        playFile.write(chunk)
playFile.close()

