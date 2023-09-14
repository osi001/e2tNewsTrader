import requests as req
from bs4 import BeautifulSoup
import pandas as pd


# response = req.get("https://uk.investing.com/")
response = req.get("https://uk.investing.com/economic-calendar/")

if response.status_code == 200:
    print("The response is gotten from the website")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    soup = BeautifulSoup(response.text, 'lxml')
    
    table = soup.find("table", class_ = "genTbl closedTbl ecoCalTbl persistArea js-economic-table")
    
    headers = table.find_all("thead", class_="floatingHeader")
    # print(headers)
    
    titles = []
    for i in headers:
        
        headings = i.find_all("th")
        title = [th.text for th in headings]
        titles.append(title)
    # print(titles)

        
    df = pd.DataFrame(columns=titles)
    # print(df)
            
    rows = table.find_all("tr")
    # print(rows)

    for i in rows [3:]:
        data = i.find_all("td")
        # print(data)
        row = [tr.text for tr in data]
        # print(row)
        l = len(df)
        df.loc[l] = row
        
        
       
    df_cleaned = df.applymap(lambda x: x.replace('\n', ''))    
   
    
    print(df_cleaned)
    df_cleaned.to_csv("economic_calender_data6.csv")
    
    
    
    #to save to sql
    # db_connection = create_engine('sqlite:///my_database.db')  # Replace with your database URL
    # # Write the DataFrame to a table in the database
    # table_name = 'my_table'
    # df.to_sql(table_name, con=db_connection, if_exists='replace', index=False)

    
    
    
    
    

