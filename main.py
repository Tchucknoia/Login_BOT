if __name__ == '__main__':
    from selenium import webdriver
    from getpass import getpass
    #import platform

    username = input('Digite seu email:')
    password = input('Digite sua senha:')

    driver = webdriver.Chrome('/home/tchucknoia/Dev/WebDrivers/chromedriver')
    driver.get('http://www.facebook.com.br')

    username_textbox = driver.find_element_by_id('email')
    username_textbox.send_keys(username)

    password_textbox = driver.find_element_by_id('pass')
    password_textbox.send_keys(password)

    login_button = driver.find_element_by_id('u_0_b')
    login_button.submit()
