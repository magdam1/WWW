# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint
import time

test_value = randint(0, 1000000)

# Funkcja pomocnicza; 
def open_and_write():
	driver1 = webdriver.Firefox()
	driver1.get("http://127.0.0.1:8000/36/192/1461/")
	driver1.find_element_by_id("edytuj_14230").click()
	form_window = driver1.find_element_by_id("form_glosy_14230")
	form_window.clear()
	form_window.send_keys(str(test_value))
	return driver1

# Test sprawdza poprawność jednostkowej operacji zapisu do bazy danych poprzez interfejs na stronie.
def test1():
	driver = open_and_write()

	driver.find_element_by_id("zapisz_14230").click()
	time.sleep(2)
	#print(driver.find_element_by_id("td_14230_głosy").text+', '+str(test_value))
	assert(driver.find_element_by_id("td_14230_głosy").text == str(test_value))
	driver.quit()

# Test sprawdza wystąpienie błędu podczas konfliktu zapisu.
def test2():
	driver1 = open_and_write()
	driver2 = webdriver.Firefox()
	driver2.get("http://127.0.0.1:8000/36/192/1461/")
	driver2.find_element_by_id("edytuj_14230").click()

	driver1.find_element_by_id("zapisz_14230").click()
	time.sleep(2)
	driver2.find_element_by_id("zapisz_14230").click()
	time.sleep(2)

	assert(driver2.find_element_by_id("tr_14230").get_attribute("class") == "red")
	driver1.quit()
	driver2.quit()

# Wywołanie testów
test1()
time.sleep(2)
test_value = randint(0, 1000000)
test2()