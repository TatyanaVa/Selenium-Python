from selenium import webdriver  
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 

from time import sleep

driver= webdriver.Firefox()
driver.get("https://www.demoblaze.com/index.html")
sleep(1)

'''login=driver.find_element(By.XPATH,'//*[@id="signin2"]')
login.click()
sleep(2)

username=driver.find_element(By.XPATH,'//*[@id="sign-username"]') 
username.send_keys('TatianaVacaITSQMET2')

password=driver.find_element(By.XPATH,'//*[@id="sign-password"]') 
password.send_keys('12345')

signup=driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/button[2]')
signup.click()

sleep(5)

alert=driver.switch_to.alert
alert.accept()
'''


ingresar=driver.find_element(By.XPATH,'//*[@id="login2"]')
ingresar.click()
sleep(2)

user=driver.find_element(By.XPATH,'//*[@id="loginusername"]') 
user.send_keys('TatianaVacaITSQMET2')

passw=driver.find_element(By.XPATH,'//*[@id="loginpassword"]') 
passw.send_keys('12345')

aceptar=driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[3]/button[2]')
aceptar.click()

sleep(5)

##SELECCIONAR PRODUCTOS

product1=driver.find_element(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[4]/div/div/h4/a')
product1.click()
sleep(1)

add_car1=driver.find_element(By.XPATH,'/html/body/div[5]/div/div[2]/div[2]/div/a')
add_car1.click()
sleep(2)

alert2=driver.switch_to.alert
alert2.accept()

home=driver.find_element(By.XPATH,'//*[@id="nava"]')
home.click()
sleep(4)

button_next=driver.find_element(By.XPATH,'//*[@id="next2"]')
button_next.click()
sleep(6)

product2=driver.find_element(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[6]/div/div/h4/a')
product2.click()
sleep(2)

add_car1=driver.find_element(By.XPATH,'/html/body/div[5]/div/div[2]/div[2]/div/a')
add_car1.click()

##CARRITO

cart=driver.find_element(By.XPATH,'//*[@id="cartur"]')
cart.click()
sleep(3)

place_order=driver.find_element(By.XPATH,'/html/body/div[6]/div/div[2]/button')
place_order.click()
sleep(1)

#DATOS DE LA ORDEN


name=driver.find_element(By.XPATH,'//*[@id="name"]') 
name.send_keys('Tatiana Vaca')

country=driver.find_element(By.XPATH,'//*[@id="country"]') 
country.send_keys('Ecuador')

city=driver.find_element(By.XPATH,'//*[@id="city"]') 
city.send_keys('Ibarra')

card=driver.find_element(By.XPATH,'//*[@id="card"]') 
card.send_keys('4401-1734-6095-2288')

month=driver.find_element(By.XPATH,'//*[@id="month"]') 
month.send_keys('08')

year=driver.find_element(By.XPATH,'//*[@id="year"]') 
year.send_keys('08')

ordenar=driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[3]/button[2]')
ordenar.click()
sleep(1)

alert=driver.switch_to.alert
alert.accept()
sleep(1)

driver.close()