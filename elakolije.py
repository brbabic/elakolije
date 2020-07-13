import requests
from bs4 import BeautifulSoup
import time
import smtplib
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup

while True:
    url = "https://elakolije.rs/svi/termini/termini-isporuke"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(response.text, "lxml")  
    result = soup.find_all('div', class_='termini_red')
    counter = 0;
    
    for res in result:
        cityWindow = "Novi Sad" in res.text
        noFreeWindow = "nema" in res.text
        freeWindow = not noFreeWindow
        if (cityWindow and freeWindow):
            counter += 1;            

    if counter is not 2:
        time.sleep(60)
        print("Continue with the script")
        
        continue

    else:
        msg = 'Subject: Univerexport elakolije notification'
        fromaddr = 'email@gmail.com'
        toaddrs  = ['email@gmail.com']
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("email@gmail.com", "password")
        print('From: ' + fromaddr)
        print('To: ' + str(toaddrs))
        print('Message: ' + msg)
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()

        break