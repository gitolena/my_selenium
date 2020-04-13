# import os
# import time
# from selenium import webdriver
# from webdriver_manager.firefox import GeckoDriverManager
#
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
# time.sleep(5)
# driver.quit()


import pytest
from selenium.webdriver import Firefox
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def browser(request):
    firefox_browser = Firefox(executable_path=GeckoDriverManager().install())
    firefox_browser.maximize_window()

    def fin():
        firefox_browser.quit()

    request.addfinalizer(fin)

    return firefox_browser


def test_search_(browser):
    browser.get('https://www.youtube.com/')
    $x("//div//*[@class='gsfi ytd-searchbox']")

    assert browser.current_url == 'https://www.youtube.com/', 'We are not inside of the Python site'