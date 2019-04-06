from bs4 import BeautifulSoup as bs
import requests as rs

def getAllUserAgents():
    """
    This method gets a list of all chrome user agents 
    """
    #webpage url where user agents will be scraped from
    wpgURL = "https://developers.whatismybrowser.com/useragents/explore/software_name/chrome/"

    #headers for this request
    headers = {
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'referer' : 'https://developers.whatismybrowser.com/useragents/explore/'
    }

    #webpage response
    wpg = rs.get(wpgURL, headers = headers, proxies = ) #Insert proxies here

    #html-parsed "soup" of page content
    useragents_Soup = bs(wpg.content, 'html.parser')

    print(useragents_Soup)



def main():

    getAllUserAgents()



if __name__ == "__main__":

    main()

#GenerateUserAgents.py