from bs4 import BeautifulSoup as bs
from bs4 import Tag
import requests
r = requests.get('http://www.bioiron.org/about/board.aspx')
soup = bs(r.content,'lxml')
headlines = soup.find_all(class_ = 'headline')
for headline in headlines:
    print headline.text +'\n\n\n'
    for sibling in headline.findNextSiblings():
        if isinstance(sibling,Tag) and sibling.has_attr('class') and 'subheadline' in sibling['class']:
            print sibling.text+'\n\n'
        
        else:
                print sibling.text+'\n'
    print '\n\n\n'
