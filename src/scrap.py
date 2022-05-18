from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

DRIVER_PATH = './chrome/chromedriver.exe'

#f = open("./urls.json","w+")
filename = "./urls.json"
listObj = []

options = Options()
options.headless = True # False
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920x1080')
options.accept_insecure_certs = True

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("https://mg.olx.com.br/regiao-de-uberlandia-e-uberaba/autos-e-pecas/carros-vans-e-utilitarios?f=p")

links = driver.find_elements_by_tag_name("a")

for link in links:

    if link.get_attribute("href") is not None:
        url = link.get_attribute("href")

        anuncio = url.split("/")
        size = len(anuncio)

        if size >= 6:
            if anuncio[5] == "carros-vans-e-utilitarios":
                #print(url)
                #f.write("["+url+"]"+",")
                # Read JSON file
                with open(filename) as fp:
                    listObj = json.load(fp)
                
                # Verify existing list
                print(listObj)

                print(type(listObj))
                
                listObj.append({
                    "anuncio": url,
                })
                
                # Verify updated list
                print(listObj)
                
                with open(filename, 'w') as json_file:
                    json.dump(listObj, json_file, indent=4, separators=(',',': '))