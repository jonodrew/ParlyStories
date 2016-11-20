from bs4 import BeautifulSoup
import urllib2
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_node("a")
G.add_nodes_from(["b","c"])
nodes = ['a','b','c']
G.add_edge(1,2)
edge = ("d", "e")
G.add_edge(*edge)
edge = ("a", "b")
G.add_edge(*edge)
# adding a list of edges:
G.add_edges_from([("a","c"),("c","d"), ("a",1), (1,"d"), ("a",2)])
# print("Nodes of graph: ")
# print(G.nodes())
# print("Edges of graph: ")
# print(G.edges())
# print(G.nodes())

#nx.draw(G,with_labels = True)
# plt.savefig("simple_path.png") # save as png
# plt.show() # display


soup = BeautifulSoup(open("/Users/jonathankerr/Google Drive/ParlyStories/House of Commons Public Bill Committee _ Trade Union Bill (15 October 2015).htm"),'lxml')
spans = soup.find_all('span', attrs={'class':'hs_CLMember'})

def scrapePage(url):
    soup = BeautifulSoup(page.read(),'lxml')
    links = []
    soup = soup.find_all('td', attrs = {'class' : "bill-item-description"})
    for td in soup:
        for a in td.find_all('a'):
            url = a.get('href')
            print url
            links.append(url)
    return links


url = "http://services.parliament.uk/bills/2015-16/tradeunion/stages.html"
page = urllib2.urlopen(url)

#print soup2
def findSpeakers(sections,tag,kind):
    speakers = sections.find_all(tag, {'class' : kind})
    speaker_list = set()
    for span in speakers:
        speaker = str(span.contents[0])
        speaker = speaker.replace('\n',' ')
        #speaker = speaker.replace('u'','')
        speaker_list.add(speaker)
    return speaker_list

def exploreContent(links):
    big_pot_of_speakers = []
    for a in links:
        page = urllib2.urlopen(a)
        soup = BeautifulSoup(page.read(), 'lxml')
        sections = soup.find('div', id = "mainTextBlock")
        witnesses = findSpeakers(sections,'p','hs_CLPara')
        for witness in witnesses:
            print witness
        witnesses = [x for x in witnesses if x.strip()]
        print witnesses
        MPs = findSpeakers(sections,'span','hs_CLMember')
        MPs = [x for x in MPs if x.strip()]
        new_MPs = []
        for MP in MPs:
            MP = MP.replace(":","")
            new_MPs.append(MP)
        MPs = new_MPs
        for MP in reversed(MPs):
            print MP
            if ',' in MP:
                MPs.remove(MP)
                print "Removed %s" % MP
            else:
                print "Did not remove %s" % MP
        print MPs
        neo_MP_list = []
        initials_list = []
        for i in MPs:
            initials = ''.join(name[0].lower() for name in i.split())
            initials_list.append(initials)
            print "CREATE (%s:Person {name: %s})" % (initials,repr(i))
        for i in MPs:
            initials = ''.join(name[0].lower() for name in i.split())
            print "MATCH (%s:Person),(tub:Bill)\nCREATE (%s)-[r:SPOKE_ON]->(tub)" % (initials,initials)
        witnesses = sections.find_all('span', {'class' : 'hs_CLPara'})
        witness_list = set()
        for span in witnesses:
            witness = str(span.contents[0])
            witness = witness.replace('\n',' ')
            #speaker = speaker.replace('u'','')
            witness_list.add(witness)
            print witness
    return MPs

test_urls = ['http://www.publications.parliament.uk/pa/cm201516/cmpublic/tradeunion/151013/am/151013s01.htm']
a = exploreContent(test_urls)
G1 = nx.Graph()
G1.add_nodes_from(a)
pos=nx.spring_layout(G)
#nx.draw_networkx_nodes(G,nodelist=a,node_color='r',node_size=50,alpha=0.8)
for node in a:
    G1.add_edge(node,'Trade\nUnion\nBill\nCommittee Stage')
print G1.nodes()
nx.draw(G1,with_labels=True)
plt.show()



"""
for div in divtag:
    links = div.find_all('a')
    for a in links:
        print a
#print divtag
link_soup = []

for a in divtag:
    anchor = divtag.find('a').get('href')
    print anchor
print "Link soup!"
print link_soup

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
