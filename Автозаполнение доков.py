import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys


s = Service('C:/Test/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://qa.neapro.site/login")

#изм. окно

driver.maximize_window()


driver.find_element(By.CSS_SELECTOR, '.fieldset:nth-child(1) input').send_keys("mexx0174@gmail.com") #логин
driver.find_element(By.CSS_SELECTOR, '.fieldset:nth-child(2) input').send_keys("123456") #пароль
driver.find_element(By.CSS_SELECTOR, '.btn').click()

time.sleep(3)


driver.find_element(By.CSS_SELECTOR, ".form:nth-child(2) .document-tile:nth-child(1) > .document-name").click()


#заполнение формы пас

driver.find_element(By.ID,'surname').send_keys(Keys.PAGE_DOWN)

#фам
driver.find_element(By.ID, 'surname').clear()
driver.find_element(By.ID, 'surname').send_keys('Губайдуллин')
#имя
driver.find_element(By.ID, 'name').clear()
driver.find_element(By.ID, 'name').send_keys('Ильдар')
#отч
driver.find_element(By.ID, 'patronymic').clear()
driver.find_element(By.ID, 'patronymic').send_keys('Владиславович')
#дата рож
driver.find_element(By.NAME, "date").click()
driver.find_element(By.NAME, "date").clear()
driver.find_element(By.NAME, "date").send_keys("02.10.2000")
#серия
driver.find_element(By.ID, "passportSeries").click()
driver.find_element(By.ID, "passportSeries").clear()
driver.find_element(By.ID, "passportSeries").send_keys('99-99')
#номер
driver.find_element(By.ID, "passportNumber").click()
driver.find_element(By.ID, "passportNumber").clear()
driver.find_element(By.ID, "passportNumber").send_keys("999999")
#дата выдачи
driver.find_element(By.CSS_SELECTOR, "#dateOfIssue .mx-input").click()
driver.find_element(By.CSS_SELECTOR, "#dateOfIssue .mx-input").clear()
driver.find_element(By.CSS_SELECTOR, "#dateOfIssue .mx-input").send_keys("01.01.2015")
#код подраз
driver.find_element(By.ID, "code").click()
driver.find_element(By.ID, "code").clear()
driver.find_element(By.ID, "code").send_keys("999-999")
#снилс
driver.find_element(By.ID, "cardId").click()
driver.find_element(By.ID, "cardId").clear()
driver.find_element(By.ID, "cardId").send_keys("999-999-999 99")
#кем выдан
driver.find_element(By.ID, "issued").clear()
driver.find_element(By.ID, "issued").send_keys("УФМС г.Челябинск")
#адрес
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").click()
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys(Keys.CONTROL+"a")
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys(Keys.DELETE)
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys('г Челябинск, пр-кт Победы, д 2')
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '.vue-dadata__suggestions').click()


#номер тел
driver.find_element(By.ID, "phone").click()
driver.find_element(By.ID, "phone").clear()
driver.find_element(By.ID, "phone").send_keys("(999)999-99 99")

#чек бокс
driver.find_element(By.ID,'privacy').click()
driver.find_element(By.ID,'privacy').click()
#добав файлов

driver.find_element(By.CSS_SELECTOR, ".upload-widget > input").send_keys("C:/Test/Глоссарий.pdf")
time.sleep(2)
#принять
driver.find_element(By.CSS_SELECTOR, "button.btn:nth-child(2)").click()
time.sleep(2)

#Админка

driver.get("https://adminqa.neapro.site/login")
time.sleep(2)
driver.find_element(By.ID,'admin_email').send_keys('moderat@neapro.ru')
driver.find_element(By.ID,'admin_password').send_keys('Aa123456')
driver.find_element(By.NAME, 'commit').click()

time.sleep(1)
driver.get("https://adminqa.neapro.site/users/1971")
time.sleep(2)



time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'.documents_passport').click()
driver.find_element(By.CSS_SELECTOR,".select2-search__field").send_keys('Принят')
driver.find_element(By.CSS_SELECTOR,".select2-search__field").send_keys(Keys.ENTER)


time.sleep(5)
#Выход


driver.get('https://qa.neapro.site/schedule')

time.sleep(2)

driver.find_element(By.CSS_SELECTOR, ".scrollmenu").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".logout_name").click()

time.sleep(4)


#Удаление доков

driver.get("https://adminqa.neapro.site/users/1971")
time.sleep(2)

driver.find_element(By.XPATH, "//div[@data-model='documents_passport']//span").click()
driver.find_element(By.CSS_SELECTOR,".select2-search__field").send_keys('Ожидание')
driver.find_element(By.CSS_SELECTOR,".select2-search__field").send_keys(Keys.ENTER)


