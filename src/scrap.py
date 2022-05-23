from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import time 

DRIVER_PATH = './chrome/chromedriver.exe'

filename = "./urls.json"
listObj = []

options = Options()
options.headless = True # False
options.accept_insecure_certs = True

options.add_argument("--window-size=1920,1080")
options.add_argument("--no-sandbox")
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--disable-crash-reporter")
options.add_argument("--disable-extensions")
options.add_argument("--disable-in-process-stack-traces")
options.add_argument("--disable-logging")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--log-level=3")
options.add_argument("--output=/dev/null")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

for route in list(range(1,100)):

    print('\nLink line: ' + str(route)+'\nRoute Url: https://mg.olx.com.br/regiao-de-uberlandia-e-uberaba/autos-e-pecas/carros-vans-e-utilitarios?f=p&o='+str(route)+'\n')
    print('----------------------\n')

    driver.get("https://mg.olx.com.br/regiao-de-uberlandia-e-uberaba/autos-e-pecas/carros-vans-e-utilitarios?f=p&o="+str(route))

    links = driver.find_elements_by_tag_name("a")

    for link in links:

        if link.get_attribute("href") is not None:
            url = link.get_attribute("href")

            anuncio = url.split("/")
            size = len(anuncio)

            if size >= 6:
                if anuncio[5] == "carros-vans-e-utilitarios":
                    with open(filename) as fp:
                        listObj = json.load(fp)
                    
                    listObj.append({
                        "page": str(route),
                        "anuncio": url,
                    })
                    
                    with open(filename, 'w') as json_file:
                        json.dump(listObj, json_file, indent=4, separators=(',',': '))
        else:
            print('\nLink: ' + str(link)+'\n')
            print('----------------------\n')

    time.sleep(15)
    
time.sleep(5)
