def test_find_element_selenium(browser):
    browser.get('http://the-internet.herokuapp.com/')
    file_upload_link = browser.find_element_by_link_text('File Upload')
    print(file_upload_link)
    browser.refresh()
    file_upload_link = browser.find_element_by_link_text('File Upload')
    print(file_upload_link)
    file_upload_link.click()
    button_upload = browser.find_element_by_id('file-submit')
    assert 'Upload' == button_upload.get_attribute('value')

