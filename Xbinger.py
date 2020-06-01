import requests,sys
from bs4 import BeautifulSoup as S
from multiprocessing import Pool
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d","--dork",help="This is dork")
parser.add_argument("-p","--page",help="This is page numbers")
parser.add_argument("-o","--output",help="to save output")
args = parser.parse_args()

c = "\033[036m"
w = "\033[037m"
r = "\033[031m"
def banner():
    banner = '''
{r}   _  __{w} __    _
{r}  | |/ /{w}/ /_  (_)___  ____ ____  _____
{r}  |   /{w}/ __ \/ / __ \/ __ `/ _ \/ ___/
{r} /   |{w}/ /_/ / / / / / /_/ /  __/ /
{r}/_/|_/{w}_.___/_/_/ /_/\__, /\___/_/
                   /____/

{r}Github{c}: https://github.com/rootktz/Xbinger{w}
    '''.format(r=r,c=c,w=w)
    print(banner)

banner()
try:
    dork = args.dork
    page = args.page
    output = args.output
    if dork:
        print('[{}*{}] dork: '.format(r,w)+''+dork)
    else:
        pass
    if page:
        print('[{}*{}] page: '.format(r,w)+''+page)
    else:
        pass
    if output:
        print('[{}*{}] output: '.format(r,w)+''+output)
    else:
        pass
    headers  = { 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0' }
    m_list = []
    i = 1
    for i in range(int(page)):
        url = "http://www.bing.com/search?q="+dork+'&first='+str(i * 10 + 1)+'&FORM=PORE'
        i += 1
        m_list.append(url)

except:
    print('''Usage:
(eg.1)python3 Xbinger.py -d "inurl:php?id= site:th" -p 2 -o test.txt(With quotes)
(eg.2)python3 Xbinger.py -d inurl:php?id -p 3 -o test2.txt(Without quotes)
(eg.3)python3 Xbinger.py -d inurl:php?id -p 3(Without output )
    ''')



def filesave(output,save):
    file = open(output,'a')
    file.write(save+'\n')
    file.close()


def req(url):
    req = requests.get(url,headers = headers)
    bs = S(req.text, 'html.parser')
    results = bs.findAll('cite')
    for result in results:
        print('[{}*{}]'.format(c,w)+' '+result.text)
        if output:
            filesave(output,result.text)
        else:
            pass
if __name__ == '__main__':
    p = Pool(50)
    p.map(req,m_list)
    p.close()
    p.join()
