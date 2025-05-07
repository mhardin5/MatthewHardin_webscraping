import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

random_chapter = random.randrange(1, 22)

if random_chapter < 10:
    random_chapter = '0' + str(random_chapter)
else:
    random_chapter = str(random_chapter)

url = 'https://ebible.org/asv/JHN'+ random_chapter + '.htm'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)

page_verses = soup.findAll('div', class_='p')

myverses = []

for section_verses in page_verses:
    verse_list = section_verses.text.split('.')

    for v in verse_list:
        myverses.append(v)

mychoice = random.choice(myverses)

mychoice = f'Chapter: {random_chapter} Verse: {mychoice}'

print(mychoice)

from vonage import Vonage, Auth
from vonage_sms import SmsMessage, SmsResponse

vonage_client =  Vonage(auth=Auth(api_key="0323d3e5", api_secret="BuZ3LEBe8eOXSV6t"))
                        
#client = vonage.Client(key="0323d3e5", secret="BuZ3LEBe8eOXSV6t")
#sms = vonage.Sms(client)

message = SmsMessage(to='18324210823', from_=, text=mychoice)
response: SmsResponse = vonage_client.sms.send(message)

print(response.model_dump(exclude_unset=True))