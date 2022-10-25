from faulthandler import is_enabled
from multiprocessing.util import is_exiting
from turtle import isvisible
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import time

def esta_na_hora(hora, minuto, segundos, data_atual):
    if data_atual.hour == hora and data_atual.minute == minuto and data_atual.second == segundos:
        return True
    return False

def processa_dias_da_semana(dias_da_semana):
    dias_da_semana_int = []
    for dia in dias_da_semana:
        if dia == "seg":
            dias_da_semana_int.append(0)
        if dia == "ter":
            dias_da_semana_int.append(1)
        if dia == "qua":
            dias_da_semana_int.append(2)
        if dia == "qui":
            dias_da_semana_int.append(3)
        if dia == "sex":
            dias_da_semana_int.append(4)
        if dia == "sab":
            dias_da_semana_int.append(5)
        if dia == "dom":
            dias_da_semana_int.append(6)
    return dias_da_semana_int

def esta_no_dia_da_semana(dias_da_semana, data_atual):
    if data_atual.weekday() in dias_da_semana:
        return True

    return False

print("+++++++++++++++++++++++++++++++")
print("+++++++Agenda Prenot@mi++++++++")
print("+++++++++++++++++++++++++++++++")

hora_string = input("Que horas quer agendar? (hh:mm:sg): ")

dia_da_semana_string = input(
    "Quais dias da semana? (seg ter qua qui sex sab dom): ")
email = input("Digite seu email cadastrado: ")
senha = input("Digite sua senha: ")

hora = int(hora_string.split(':')[0])
minuto = int(hora_string.split(':')[1])
segundos = int(hora_string.split(':')[2])

dias_da_semana = dia_da_semana_string.split(' ')
dias_da_semana_int = processa_dias_da_semana(dias_da_semana)

ativo = True
while ativo:
    agora = datetime.datetime.now()
    print(agora)
    if esta_na_hora(hora, minuto, segundos, agora) and esta_no_dia_da_semana(dias_da_semana_int, agora):
        ativo = False
        navegador = webdriver.Chrome()
        navegador.get("https://prenotami.esteri.it")
        time.sleep(3)
        navegador.find_element(
            By.ID, "login-email").send_keys(email)
        navegador.find_element(
            By.ID, "login-password").send_keys(senha)
        navegador.find_element(
            By.XPATH, '//*[@id="login-form"]/button').click()
        time.sleep(3)
        navegador.find_element(By.ID, "advanced").click()
        time.sleep(2)
        navegador.find_element(
            By.XPATH, '//*[@id="dataTableServices"]/tbody/tr[2]/td[4]/a/button').click()
        time.sleep(2)
        i = 1
        while navegador.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/button') == navegador.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/button'):
            print("Tentativa Nº - " + str(i))
            navegador.find_element(
                By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/button').click()
            time.sleep(2)
            navegador.find_element(
                By.XPATH, '//*[@id="dataTableServices"]/tbody/tr[2]/td[4]/a/button').click()
            i = i + 1
    time.sleep(1)
time.sleep(1)
navegador.find_element(By.ID, 'File_0').click()
time.sleep(4)
navegador.find_element(By.ID, 'PrivacyCheck').click()
navegador.find_element(By.ID, 'btnAvanti').click()
ativo = True
while ativo:
    if navegador.find_element(By.CLASS_NAME, 'day availableDay').is_enabled:
        navegador.find_element(By.CLASS_NAME, 'day availableDay').click()
        ativo = False
navegador.find_element(By.CLASS_NAME, 'table-condensed > dtpicker-next').click()
navegador.find_element(By.ID, 'btnPrenota').click()