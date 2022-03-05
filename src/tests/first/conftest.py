import pytest
from appium import webdriver


@pytest.fixture()
def driver():
    desired_capabilities = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "platformVersion": "8.0",
        "automationName": "Appium",
        "appPackage": "org.wikipedia",
        "appActivity": ".main.MainActivity",
        "app": "C:\\LearnQA\\avt-mob-50-python\\apks\\\org.wikipedia.apk"
    }

    driver = webdriver.Remote(command_executor= 'http://127.0.0.1:4723/wd/hub',
                              desired_capabilities=desired_capabilities)
    yield driver

    driver.quit()
