import pytest
from selene import browser, be, have


@pytest.fixture
def browser_size():
    browser.config.window_height = 1080
    browser.config.window_width = 720


def test_valid_search(browser_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))
    print('Результаты поиска присутствуют')


def test_not_valid_search(browser_size):
    browser.open('https://google.com')
    string_search = 'sdfg345678dfghj'
    browser.element('[name="q"]').should(be.blank).type(string_search).press_enter()
    browser.element('[style="padding-top:.33em"]').should(have.text(f'По запросу {string_search} ничего не найдено'))
    print('Результаты поиска отсутствуют')
