# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

import sys
import os
import pdb
import re

class Spider():

    def __init__(self):

        self.screen_shots_path = './screenshot.png'

# Ubicacion del chromedriver

        chrome_driver_path = "/usr/bin/chromedriver" 
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("window-size=1920,1080")

        self.driver = webdriver.Chrome(chrome_driver_path, chrome_options=chrome_options)
        self.timeout = 30



    def run(self):
        try:

            urls = ['http://www.yasni.es/', 'https://webmii.com/','https://www.pipl.com/',
                    'https://www.spokeo.com/']

            name = input('Introduce el nombre/nickname que quieras investigar: ')
            for url in urls:
                self.driver.get(url)  # Método para acceder a una URL
                try:
                    f = open("Busqueda_{name}.txt".format(name=name), "w")
                    self.output_file = '/home/ubuntu/Busqueda_{name}.txt'.format(name=name)
                    with open(self.output_file, 'w') as out_file:
                        out_file.write("************************ INFORMACION DE YASNI ****************************************\n")

                    if url == 'http://www.yasni.es/':
                        try:
                            print('Buscando en yasni....')
                            input_name = self.driver.find_element_by_xpath('//*[@id="searchfield3"]')
                            input_name.clear()
                            input_name.send_keys(name)
                            self.driver.find_element_by_xpath('//*[@id="main-content-center-frontpage"]/div[3]/div[2]/div/div[1]').click()
                            html = self.driver.page_source  # Obtenemos el HTML de la pagina web actual
                            soup = BeautifulSoup(html, "lxml")
                            links_busqueda = soup.find_all('div', {"class": "content-result-box"})
                            for link in links_busqueda:
                                link.text.strip()
                                with open(self.output_file, 'a') as out_file:
                                    out_file.write(link.text)
                                    out_file.write("---------------------------------------------------------\n")
                            f.close()
                            print('Informacion introducida en archivo.')
                        except Exception as e:
                            print(e)
                            raise
                    elif url == 'https://webmii.com/':
                        try:
                            print('Buscando en webmii....')
                            input_name = self.driver.find_element_by_xpath('//*[@id="searchName"]')
                            input_name.clear()
                            input_name.send_keys(name)
                            self.driver.find_element_by_xpath('//*[@id="searchSubmit"]').click()
                            html = self.driver.page_source  # Obtenemos el HTML de la pagina web actual
                            soup = BeautifulSoup(html, "lxml")
                            links_busqueda = soup.find_all('div', {"class": "gsc-results gsc-webResult"})
                            for link in links_busqueda:
                                link.text.strip()
                                with open(self.output_file, 'a') as out_file:
                                    out_file.write('*************************** INFORMACION DE WEBMII ***************************************\n')
                                    out_file.write(link.text)
                                    out_file.write("---------------------------------------------------------\n")
                            f.close()
                            print('Informacion introducida en archivo....')
                            break
                        except Exception as e:
                            pritn(e)
                            raise
                    elif url == 'https://www.pipl.com/':
                        try:
                            print('Buscando en pipl....')
                            input_name = self.driver.find_element_by_xpath('//*[@id="findall"]')
                            input_name.clear()
                            input_name.send_keys(name)
                            self.driver.find_element_by_xpath('/html/body/section[1]/div/div/div[2]/form/span/input').click()
                            links_busqueda = soup.find_all('div', {"class": "gsc-results gsc-webResult"})
                            for link in links_busqueda:
                                with open(self.output_file, 'a') as out_file:
                                    out_file.write("************************** INFORMACION DE PIPL ******************************************\n")
                                    out_file.write(link.text)
                                    out_file.write("---------------------------------------------------------\n")
                            f.close()
                        except Exception as e:
                            print(e)
                            raise
                    elif url == 'https://www.spokeo.com/':
                        try:
                            print('Buscando en spokeo....')
                            f.write("************************** INFORMACION DE SPOKEO ****************************************")
                            input_name = self.driver.find_element_by_xpath('//*[@id="homepage_hero_form"]/div/div[1]/div/div/input')
                            input_name.clear()
                            input_name.send_keys(name)
                            self.driver.find_element_by_xpath('//*[@id="search"]').click()
                            links_busqueda = soup.find_all('div', {"class": "gsc-results gsc-webResult"})
                            for link in links_busqueda:
                                with open(self.output_file, 'a') as out_file:
                                    out_file.write(link.text)
                                    out_file.write("---------------------------------------------------------")
                            f.close()

                        except Exception as e:
                            print(e)
                            raise # Toma una captura de pantalla
                except:
                    raise
        except:
            raise
        finally:
            self.driver.quit()

if __name__ =='__main__':
    spider = Spider()
    spider.run()




