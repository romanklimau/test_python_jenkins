from time import sleep


def test_alert_window(browser):
    browser.get("https://www.testandquiz.com/selenium/testing.html")
    alert_box_button = browser.find_element_by_xpath("//b[contains(text(),'Click button to generate Alert box')]/../button")
    alert_box_button.click()
    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()