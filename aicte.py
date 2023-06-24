from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import mysql.connector as mysql;
#import pandas as pd;
driver=webdriver.Chrome()
a=[]
b=[]
while 1:
    o=int(input("0 for stock and 1 crypto:"))
    if o==0:
          s=input("Enter company name:")
          driver.get("https://www.google.com//search?q="+s+" share price &start")
          driver.implicitly_wait(10)
          t=driver.find_element("xpath",'//*[@id="knowledge-finance-wholepage__entity-summary"]/div[3]/g-card-section/div/g-card-section/div[2]/div[1]/span[1]/span/span[1]').text
          print("Stock price of ",s,":",t)
          f=[s,t]
          a.append(f)
          conn=mysql.connect(host="localhost",user="root",passwd="Yogha@025@04",database="yogha")
          e=conn.cursor()
          sql="INSERT INTO stock VALUES('"+s+"','"+t+"')"
          e.execute(sql)
          e.execute("Commit")
          f=int(input("Do u want to continue?"))
          if f==0:
             break
    else:
        s=input("Enter crypto name:")
        driver.get("https://www.google.com//search?q="+s+" price &start")
        driver.implicitly_wait(10)
        t=driver.find_element("xpath",'//*[@id="crypto-updatable_2"]/div[3]/div[2]/span[1]').text
        print("Crypto price of ",s,":",t)
        f=[s,t]
        b.append(f)
        conn=mysql.connect(host="localhost",user="root",passwd="Yogha@025@04",database="yogha")
        e=conn.cursor()
        sql="INSERT INTO crypto VALUES('"+s+"','"+t+"')"
        e.execute(sql)
        e.execute("Commit")
        f=int(input("Do you want to continue?"))
        if f==0:
            break
print("Company name\tShare Price")
for i in a:
    print(i[0],"\t",i[1])
print("Cryptocurrency\tPrice")
for i in b:
    print(i[0],"\t",i[1])
