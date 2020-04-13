import pytest
import time
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def browser(request):
    browser = Firefox(executable_path=GeckoDriverManager().install())
    browser.maximize_window()
    browser.get("https://www.youtube.com/")
    browser.switch_to.window(browser.window_handles[0])

    def fin():
        browser.quit()

    request.addfinalizer(fin)

    return browser


def test_search_covid(browser):
    input_field = browser.find_element(
        By.XPATH, "//input[@id='search']"
    )
    search_button = browser.find_element(By.CSS_SELECTOR, "#search-icon-legacy")
    input_field.send_keys("covid19")
    search_button.click()
    time.sleep(5)

    found_item = browser.find_element(By.CSS_SELECTOR, ".ytd-clarification-renderer")
    assert found_item, "Sorry, cannot find WHO Int."

    found_item.click()
    time.sleep(5)

    browser.switch_to.window(browser.window_handles[1])
    assert browser.current_url == 'https://moz.gov.ua/koronavirus-2019-ncov'