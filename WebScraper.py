import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import time

def runRequests():
    df = pd.DataFrame(columns = ['Name','Purpose'])
    x = 0
    while(x < 51):
        try:
            print("Number of Successful Requests: ", x)
            r = requests.get("http://3.95.249.159:8000/random_company")
            soup = BeautifulSoup(r.text,"html.parser")
            name = soup.find('li', text = re.compile('Name:')).text
            purpose = soup.find('li', text = re.compile('Purpose:')).text
            row = {'Name':name[6:],'Purpose':purpose[9:]}
            df = df.append(row, ignore_index = True)
            x = x + 1
            #time.sleep(1)

        except:
            print("requests failed, will try again.")
    df.to_csv('requests_output.csv', index = False)



if __name__ == "__main__":
    runRequests()
