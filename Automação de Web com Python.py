#Instalar o webdriver

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#Criar um navegador
navegador = webdriver.Chrome(executable_path=r"./chromedriver.exe")

