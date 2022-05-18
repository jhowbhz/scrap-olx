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
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920x1080')
options.accept_insecure_certs = True

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
#driver.get("https://mg.olx.com.br/regiao-de-uberlandia-e-uberaba/autos-e-pecas/carros-vans-e-utilitarios/loucura-total-imperdivel-trailblazer-2014-automatica-muito-nova-agio-so-62-mil-reais-1005300647#")

with open(filename) as fp:
    urls_anuncios = json.load(fp)

#loop interate through the list
for url_anuncio in urls_anuncios:
    print(url_anuncio.get("anuncio"))

    driver.get(url_anuncio.get("anuncio"))

    element = driver.find_element_by_id("initial-data")
    json_text = json.loads(element.get_attribute('data-json'))

    ad = json_text.get('ad')
    user = ad.get('user')
    phone = ad.get('phone')

    f = open("contatos.txt", "a+")
    f.write('Nome: ' + str(user.get('name')) + "\n" + 'Descricao: ' + str(ad.get('body')) + "\n" + "Telefone: " + str(phone.get('phone')) + "\n" + "Verificado: " + str(phone.get('phoneVerified')) + "\n" + "Anuncio: " + str(url_anuncio.get('anuncio')) + "\n" + "\n")

    time.sleep(15)
