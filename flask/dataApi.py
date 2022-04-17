from bs4 import BeautifulSoup
import requests

def scrape(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text,"html.parser")
    #print(soup.find_all('size'))
    pageTxt = soup.get_text()
    #print(pageTxt)

    words = pageTxt.split(" ")


    metaList = []

    for x in range(len(words)):
        #print(words[x])
        if "Discovery" in words[x]:
            metaList.append(words[x])
        if("Total" in words[x]):
            for i in range(x, x+5):
                metaList.append(words[i])
            # break

    # 		break
    cite = ""
    for word in metaList:
        cite = cite + " " +word
    cite.replace("\n", " ")

    # arr = list(cite)
    # print(arr)

    return(cite)
