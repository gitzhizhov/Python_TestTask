# 1. Открыть страницу http://google.com/ncr
# 2. Выполнить поиск слова “selenide”
# 3. Проверить, что первый результат – ссылка на сайт selenide.org.
# 4. Перейти в раздел поиска изображений
# 5. Проверить, что первое изображение неким образом связано с сайтом selenide.org.
# 6. Вернуться в раздел поиска Все
# 7. Проверить, что первый результат такой же, как и на шаге 3.


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

targetPage = 'http://www.google.com/ncr'
xpath = ''
query = 'selenide'
queryTest = 'selenide.org'

driver = webdriver.Chrome()
driver.get(targetPage)

# открытие страницы google, нахождение строки поиска, ввод строки запроса
def setUp():
    assert 'Google' in driver.title
    elem = driver.find_element(By.NAME, "q")
    elem.send_keys('selenide')
    elem.send_keys(Keys.RETURN)
    assert 'No results found.' not in driver.page_source

# основное выполнение
def searchQ():
    setUp()
    
    listRes = driver.find_elements(By.PARTIAL_LINK_TEXT, queryTest) #сайт
    checkRes(listRes)
        
    buttonPic = driver.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div/div[2]/a') #переход на элемент Картинки
    click(buttonPic)
    time.sleep(1)
    
    imgRes = driver.find_elements(By.XPATH, '//*[@id="islrg"]/div[1]/div[1]/a[2]') #картинка 
    checkRes(imgRes)

    buttonAll = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/div/div[1]/div[1]/div/div/a[1]') # переход на элемент Все
    click(buttonAll)
    time.sleep(1)
    
    listRes = driver.find_elements(By.PARTIAL_LINK_TEXT, queryTest) #сайт
    checkRes(listRes)

# переход по переданному пути
def click(path):
    path.click()
    
# проверка результата
def checkRes(listRes,):
    for i in listRes:
        if queryTest in i.text:
            print(f'Сайт\картинка {queryTest} присутствует в выдаче')
            break

def tearDown():
    driver.close()

searchQ()
time.sleep(1)
tearDown()
