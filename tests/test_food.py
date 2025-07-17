from selenium import webdriver
from selenium.webdriver.common.by import By

def test_01_h1():
    driver = webdriver.Chrome()
    driver.get("https://berejok3.github.io/food.html")
    assert = driver.find_element(By.TAG_NAME, "h1").text == "Простой бутерброд с сыром"

def test_02_h2():
    driver = webdriver.Chrome()
    driver.get("https://berejok3.github.io/food.html")
    assert = driver.find_element(By.TAG_NAME, "h2").text == "Что нужно"

def test_03_h3():
    driver = webdriver.Chrome()
    driver.get("https://berejok3.github.io/food.html")
    assert = driver.find_element(By.TAG_NAME, "p").text == "Хлеб, сливочное масло, сыр, зелень (по желанию)"

   driver.quit()
