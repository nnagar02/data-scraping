#Importing Necessary Libraries
import requests 
from bs4 import BeautifulSoup 
import re
from html.parser import HTMLParser
import contractions

def clean_content_as(URL):
    
    parser = "html.parser"
    
    #Cleaning functions for the HTML Content
    class MLStripper(HTMLParser):
        def __init__(self):
            self.reset()
            self.strict = False
            self.convert_charrefs= True
            self.fed = []
        def handle_data(self, d):
            self.fed.append(d)
        def get_data(self):
            return ''.join(self.fed)

    def strip_tags(html):
        s = MLStripper()
        s.feed(html)
        return s.get_data()


    def clean_html(text):
            return contractions.fix(re.sub('\[[^]]*\]', '', BeautifulSoup(text, parser).get_text())).replace("\n"," ")

    def ultimate_clean(var_string):
        t_b = BeautifulSoup(var_string,parser)
        [x.extract() for x in t_b(['script', 'style'])]
        return re.sub('[ \t\n\r]+', ' ',clean_html(t_b.get_text()))

    #Header Bot for Browser, which will not trigger non-bot allowance requests for website
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0'}

    sending_request = requests.get(URL, headers=headers)

    soup_html_content = BeautifulSoup(sending_request.content, 'html.parser') #The parser can vary according to the use case
    
    return ultimate_clean(str(soup_html_content))

