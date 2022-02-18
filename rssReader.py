import feedparser
myFeed = feedparser.parse("http://feeds.mashable.com/Mashable")

print('피드 제목: ', myFeed['feed']['title'])
print('포스트 수: ', len(myFeed.entries))

post = myFeed.entries[0]
print('포스트 제목:', post.title)

content = post.description
print('콘텐츠 원본: \n', content)


from bs4 import BeautifulSoup
html_doc = open('sample-html.html', 'r').read()
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.get_text())
print(soup.title)
print(soup.h1.string)
print(soup.img['alt'])

for p in soup.find_all('p'):
    print(p.string)

