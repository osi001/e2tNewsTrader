import requests as req
from bs4 import BeautifulSoup


# response = req.get("https://uk.investing.com/")
response = req.get("https://uk.investing.com/economic-calendar/")

if response.status_code == 200:
    print("The response is gotten from the website")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    
    # all_para = soup.find_all('p')
    
    # all_links = soup.find_all('a')
    
    # for link in all_links:
    #     print(link)
    
    
    
    for section in soup.find_all("table", {'id': 'economicCalendarData'}):
        print (section.find("tbody").text)
        
        
        
    # for section in soup.find_all("table", {'id': 'economicCalendarData'}):
    #     if (section.find("tbody").text) == "Unemployment Rate":
    #         print (section)
        
    # calenderData = soup.find('table', {'id': 'economicCalendarData'})
    # print(calenderData)
        

