import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='es',
                     help="Choose lang")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()

# Така как в задаии указано то что достаточно того чтобы код работал только для браузера Сhrome, в conftest.py оставил только
# обработчик считования параметра language из командной строки