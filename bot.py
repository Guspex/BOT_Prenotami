from selenium import webdriver
from selenium.webdriver.common.by import By

import time

navegador = webdriver.Chrome()
navegador.get("https://prenotami.esteri.it")
time.sleep(4)
navegador.find_element(By.ID, "login-email").send_keys("Seu email cadastrado")
navegador.find_element(By.ID, "login-password").send_keys("Sua senha cadastrada")
navegador.find_element(By.XPATH, '//*[@id="login-form"]/button').click()
time.sleep(5)
navegador.find_element(By.ID, "advanced").click()
time.sleep(2)
navegador.find_element(By.XPATH, '//*[@id="dataTableServices"]/tbody/tr[2]/td[4]/a/button').click()
time.sleep(2)
i = 1
while navegador.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/button') == navegador.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/button'):
        print("Tentativa Nº - " + str(i))
        navegador.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/button').click()
        time.sleep(4)
        navegador.find_element(By.XPATH, '//*[@id="dataTableServices"]/tbody/tr[2]/td[4]/a/button').click()
        i = i + 1