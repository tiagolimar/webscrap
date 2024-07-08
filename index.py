from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd

drive = webdriver.Chrome(service = Service(ChromeDriverManager().install()))

URL = "https://www.tigre.com.br/produto/uniao-soldavel"

drive.get(URL)

PATH = '/html/body/div[1]/div/div[2]/main/div/section[2]/div/div/div/div/div[1]/div/div/table'

elemento = drive.find_element('xpath', PATH)

html_tabela = elemento.get_attribute('outerHTML')

tabela = pd.read_html(str(html_tabela), thousands='.', decimal=',')[0]

print(tabela['Código'])
