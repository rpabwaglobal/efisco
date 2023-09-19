from utilities.bot_setup import BotSetup
from selenium.webdriver.common.by import By
from .locators import LOCATORS
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging
from threading import Thread
#from images.images import IMAGES
#from utilities.pag import *
import json
import requests
from time import sleep

import pandas as pd

class EfiscoBase(BotSetup):
    
    def abrir_sistema_efisco(self): 
        self.driver.get("https://efisco.sefaz.pe.gov.br/sfi_com_sca/PRMontarMenuAcesso")
        logging.info("sistema efisco pronto para uso")

    
    def login_efisco(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LOCATORS["BUTTON"]["ENTRAR_COM_GOV"]))
        self.driver.find_element(*LOCATORS["BUTTON"]["ENTRAR_COM_GOV"]).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LOCATORS["BUTTON"]["LOGIN_CERT_DIGITAl"]))
        certificado = (IMAGES["PAINEL"]["CERTIFICADO"])
        self.__logar_com_certificado(certificado)
        self.driver.find_element(*LOCATORS["BUTTON"]["LOGIN_CERT_DIGITAl"]).click()
        logging.info("login com certificado realizado com sucesso")
    
    def __selecionar_certificado(self):
        if exists(IMAGES["PAINEL"]["CERTIFICADO"]):
            double_click(IMAGES["PAINEL"]["CERTIFICADO"])
    
    def __logar_com_certificado(
        self,
        base,
        block_execution=False,
    ):
        certificate_selector = Thread(target=self.__selecionar_certificado, args=[])
        certificate_selector.start()
        if block_execution:
            certificate_selector.join()
    
    