from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import json
import time 

DRIVER_PATH = './chrome/chromedriver.exe'
filename = "./urls.json"

f = open("contatos.txt", "a+")

options = Options()
options.headless = True # False

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
#driver.get("https://mg.olx.com.br/regiao-de-uberlandia-e-uberaba/autos-e-pecas/carros-vans-e-utilitarios/loucura-total-imperdivel-trailblazer-2014-automatica-muito-nova-agio-so-62-mil-reais-1005300647#")

with open(filename) as fp:
    urls_anuncios = json.load(fp)

for url_anuncio in urls_anuncios:

    print(url_anuncio.get("anuncio")+'\n')
    print('--------------------\n')

    driver.get(url_anuncio.get("anuncio"))

    if(driver.title != 'Anúncio não encontrado | OLX'):

        element = driver.find_element_by_id("initial-data")
        if( element is not None):
            json_text = json.loads(element.get_attribute('data-json'))

            ad = json_text.get('ad')

            if(ad is not None):
                user = ad.get('user')
                phone = ad.get('phone')

                f = open("contatos.txt", "a+")
                f.write('Nome: ' + str(user.get('name')) + "\n" + 'Descricao: ' + str(ad.get('body')) + "\n" + "Telefone: " + str(phone.get('phone')) + "\n" + "Verificado: " + str(phone.get('phoneVerified')) + "\n" + "Anuncio: " + str(url_anuncio.get('anuncio')) + "\n" + "\n")
            else:
                print("Não encontrado")
                f = open("contatos.txt", "a+")
                f.write('Anuncio vazio: ' + str(url_anuncio.get('anuncio')) + "\n" + "\n")

    else:
        print('Anuncio nao encontrado')
        f = open("contatos.txt", "a+")
        f.write('Anuncio nao encontrado: ' + str(url_anuncio.get('anuncio')) + "\n" + "\n")

time.sleep(25)
