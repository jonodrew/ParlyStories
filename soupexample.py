from bs4 import BeautifulSoup
import urllib2

soup = BeautifulSoup(open("/Users/jonathankerr/Google Drive/ParlyStories/House of Commons Public Bill Committee _ Trade Union Bill (15 October 2015).htm"),'lxml')
spans = soup.find_all('span', attrs={'class':'hs_CLMember'})

url = "http://services.parliament.uk/bills/2015-16/tradeunion/stages.html"
page = urllib2.urlopen(url)
soup2 = BeautifulSoup(page.read(),'lxml')
#print soup2
links = []
soup3 = soup2.find_all('td', attrs = {'class' : "bill-item-description"})
for td in soup3:
    for a in td.find_all('a'):
        url = a.get('href')
        links.append(url)
big_pot_of_speakers = []
for a in links:
    #print a
    page = urllib2.urlopen(a)
    soup = BeautifulSoup(page.read(), 'lxml')
    div = soup.find('div', id = "content").h3
    print div
    """
    output = set()
    for span in spans:
        speaker = str(span.contents[0])
        speaker = speaker.replace('\n',' ')
        #speaker = speaker.replace('u'','')
        output.add(speaker)
"""

"""
for div in divtag:
    links = div.find_all('a')
    for a in links:
        print a
#print divtag
link_soup = []
"""
"""
for a in divtag:
    anchor = divtag.find('a').get('href')
    print anchor
print "Link soup!"
print link_soup
"""
    #link_soup = soup2.find_all('a')
"""
speakers = []

link_soup2 = BeautifulSoup(page.read(),'lxml')
for link in link_soup2:
    anchor = link.get('href')
    print anchor
output = set()
for span in spans:
    speaker = str(span.contents[0])
    speaker = speaker.replace('\n',' ')
    #speaker = speaker.replace('u'','')
    output.add(speaker)


for speaker in speakers:
    output.add(speaker)
print output
"""
