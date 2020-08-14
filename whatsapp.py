from selenium import webdriver

driver = webdriver.Chrome("path/chromedriver.exe")
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group : ')
msg = input('Enter your message : ')
count = int(input('Enter the count : '))

input('Enter anything after scanning QR code')

search = driver.find_element_by_class_name('_3FRCZ')
search.send_keys(name)

user = driver.find_element_by_class_name('eJ0yJ')
user.click()

msg_box = driver.find_elements_by_class_name('_3FRCZ')

for i in range(count):
    msg_box[1].send_keys(msg)
    button = driver.find_element_by_class_name('_1U1xa')
    button.click()
