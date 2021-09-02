from __future__ import unicode_literals
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_show_my_pets():
    pytest.driver = webdriver.Chrome('C:\soft\chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends1.herokuapp.com/login')
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('ilyavas.0@mail.ru')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('snorkilus')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    WebDriverWait(pytest.driver, 4).until(EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "PetFriends"));

    assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"
    # Переходим на страницу Мои питомцы
    pytest.driver.find_element_by_css_selector('#navbarNav [href="/my_pets"]').click()
    # Получаем данные, нужные нам для тестов и по заданию практикума добавляем ожидания для всех элементов
    pytest.driver.implicitly_wait(1)
    images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
    pytest.driver.implicitly_wait(1)
    names = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
    pytest.driver.implicitly_wait(1)
    descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
    pytest.driver.implicitly_wait(1)
    ages = pytest.driver.find_elements_by_xpath('//tbody/tr/td[3]')

    # Часть из 25.3 проверяет правильность всех питомцев
    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0

    # количество строк в таблице с данными питомцев
    all_my_pets = pytest.driver.find_elements_by_xpath('//tbody/tr')
    # количество питомцев в статистике пользователя
    count_of_my_pets = pytest.driver.find_element_by_xpath('//*[h2][1]').text.split()
    # совпадает ли число моих питомцев в статистике пользователя
    # с реальным количеством строк в таблице с данными питомцев
    assert len(all_my_pets) == int(count_of_my_pets[(2)])

    # количество питомцев с фото
    count_images = len(pytest.driver.find_elements_by_tag_name('img'))

    # более чем у половины питомцев есть фото 25.3.1.2
    assert (count_images - 1) / len(all_my_pets) > .5

    pytest.driver.quit()

    # у всех имена,возраст,парода не пустые
    for i in range(len(names)):
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ages[i].text != ''

    # У всех питомцев разные имена
    i = 0
    while i < len(names):
        j = i + 1
        while j < len(names):
            assert names[i].text != names[j].text
            j += 1
        i += 1

    # В списке нет повторяющихся питомцев 25.3.1.5
    i = 0
    while i < len(names):
        j = i + 1
        while j < len(names):
            assert not (names[i].text == names[j].text and descriptions[i].text == descriptions[j].text and
                        ages[i].text == ages[j].text)
            j += 1
        i += 1