from itertools import dropwhile

from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.by import By

# Dane testowe
DATA_EMAIL = "kdhfsjdh@spam.la"

# Stworzenie instancji klasy Chrome
# (to otworzy przeglądarkę)
driver = Chrome()
# Otwarcie strony
driver.get("https://automationpractice.techwithjatin.com/")

# Maksymalizacja okna
driver.maximize_window()
# Znajdz element Sign in
sign_in_a = driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in")
# Kliknij w odnaleziony element
sign_in_a.click()

# Wpisz email
driver.find_element(By.ID, "email_create").send_keys(DATA_EMAIL)

sleep(5)
driver.quit()

