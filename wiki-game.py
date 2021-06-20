import requests
from bs4 import BeautifulSoup

def find_target(path, target, N):
    # In case of external/incompatible links
    try:
        src = requests.get(path[-1])
    except:
        return False
    soup = BeautifulSoup(src.text, 'html.parser')
    links = list()
    for paragraphs in soup.find_all('p'):
        for urls in paragraphs.find_all('a'):
            if "/wiki/" not in str(urls):
                continue
            links.append(urls['href'])
    if N>1:
        for link in links:
            if find_target(path+[wiki_base+link], target, N-1):
                return True
    if N==1:
        for link in links:
            if target == link:
                print("Done!\n")
                for p in path:
                    print(p)
                print(wiki_base+target)
                print(len(path))
                return True
        return False

wiki_base = "https://en.wikipedia.org"
target = "/wiki/Python_(programming_language)"

begin_url = input("Enter Wiki URL:")

if begin_url == wiki_base+target:
    print("Easy done!")
    exit()

path = [begin_url.strip()]
i=1
while not find_target(path, target, i):
    i+=1
    print(i)