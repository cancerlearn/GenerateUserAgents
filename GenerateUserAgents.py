from bs4 import BeautifulSoup as bs
import requests as rs
import GenerateProxyIP as genIP

def getAllUserAgents():
    """
    This method gets a list of all chrome user agents from the webpage "https://developers.whatismybrowser.com/useragents/explore/software_name/chrome/"
    """
    #webpage url where user agents will be scraped from
    wpgURL = "https://developers.whatismybrowser.com/useragents/explore/software_name/chrome/"

    #headers for this request
    headers = {
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'referer' : 'https://developers.whatismybrowser.com/useragents/explore/'
    }

    #webpage response
    wpg = rs.get(wpgURL, headers = headers, proxies = genIP.getRandomProxyIPDict(), timeout = 5)

    #check if request was successful
    if (wpg.status_code != 200):
        print("status code not 200", "status code is", wpg.status_code)
        return

    #html-parsed "soup" of page content
    useragents_Soup = bs(wpg.content, 'html.parser')

    userAgentTable = useragents_Soup.select("div.corset>table.table-useragents>tbody>tr")

    #print(userAgentTable)

    for row in userAgentTable:

        print(row.select_one("td.useragent>a").string)



def main():

    getAllUserAgents()



if __name__ == "__main__":

    main()

#GenerateUserAgents.py