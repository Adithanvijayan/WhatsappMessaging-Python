from selenium import webdriver

driver = webdriver.Chrome("path/chromedriver.exe")
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group : ')
msg = input('Enter your message : ')
count = int(input('Enter the count : '))

input('Enter anything after scanning QR code')

search = driver.find_element_by_class_name('_2S1VP')
search.send_keys(name)

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_elements_by_class_name('_2S1VP')

for i in range(count):
    msg_box[1].send_keys(msg)
    button = driver.find_element_by_class_name('_35EW6')
    button.click()