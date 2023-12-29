from selenium import webdriver
import time

from selenium.webdriver.common.by import By

url = 'https://zakupki.gov.ru/epz/main/public/home.html'
driver = webdriver.Chrome()
try:
    driver.get(url=url)
    time.sleep(5)
    btnCancellation = driver.find_element(By.XPATH, "//*[@class='btn btn-default w-100']")
    btnCancellation.click()
    time.sleep(3)
    procurement = driver.find_element(By.XPATH, "//*[@class='main-link  _order ']")
    procurement.click()
    time.sleep(1)
    typePurchase = driver.find_element(By.XPATH, "//*[@class='col-9 p-0 registry-entry__header-top__title "
                                                 "text-truncate']").text
    numNotification = driver.find_element(By.XPATH, "//*[@class='registry-entry__header-mid__number']//*").text
    objectPurchase = driver.find_element(By.XPATH, "//*[@class='registry-entry__body-value']").text
    customer = driver.find_element(By.XPATH, "//*[@class='registry-entry__body-href']//*").text
    startingPrice = driver.find_element(By.XPATH, "//*[@class='price-block__value']").text

    print("Тип закупки: " + typePurchase)
    print("Номер извещения: " + numNotification)
    print("Объект закупки: " + objectPurchase)
    print("Заказчик: " + customer)
    print("Начальная цена: " + startingPrice)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
