import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
from datetime import datetime


@pytest.fixture()
def setup():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    return driver


def pytest_configure(config):
    # _metadata only exists when pytest metadata plugin is loaded
    if hasattr(config, '_metadata'):
        config._metadata['Project Name'] = 'Opencart'
        config._metadata['Module Name'] = 'CustRegistration'
        config._metadata['Tester'] = 'Tes'

    # Setting HTML report path
    try:
        config.option.htmlpath = (
            os.path.abspath(os.curdir) + "\\Reports\\" +
            datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"
        )
    except AttributeError:
        pass  # config.option not available in early hook calls


# Hook to remove unwanted metadata keys from HTML report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
