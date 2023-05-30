from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

    LOGIN_EMAIL_ADDRESS = (By.CSS_SELECTOR, "id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR,"id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[name='login_submit']")

    REGISTRATION_EMAIL_ADDRESS = (By.CSS_SELECTOR,"id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "id_registration-password1")
    REGISTRATION_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR,"[name = 'registration_submit']")