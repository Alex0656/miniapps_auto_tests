from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    EMAIL = (By.CSS_SELECTOR, "input[id='loginForm_email']")
    PASSWORD = (By.CSS_SELECTOR, "input[id='loginForm_password']")
    OPEN = (By.CSS_SELECTOR, "button[class='ant-btn css-1b1hgxe ant-btn-primary ant-btn-block']")

