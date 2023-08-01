import time
import requests
from behave import *
from selenium.webdriver import Chrome

target = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Unige.svg/1200px-Unige.svg.png"
malicious = "\'><script>alert('Hello Hacker')</script>"
url1 = "http://localhost/Assignment3/img-loader.php?target="
url2 = "http://localhost/Assignment3/img-loader-protected.php?target="
url3 = "http://localhost/Assignment3/img-loader-protected2.php?target="

malicious_url = url1 + malicious
malicious_url2 = url2 + malicious
malicious_url3 = url3 + malicious

normal_url = url1 + target
normal_url2 = url2 + target
normal_url3 = url3 + target


@given(u'enter the img-loader page')
def enter_page1(context):
    requests.get(normal_url)


@then(u'the img page will show an image')
def check3(context):
    response = requests.get(normal_url)
    assert response.status_code == 200


@given(u'enter the img-loader-protected page')
def enter_page2(context):
    context.response = requests.get(normal_url2)


@then(u'the img protected page will show an image')
def check1(context):
    response = requests.get(normal_url2)
    assert response.status_code == 200


@given(u'enter the img-loader-protected2 page')
def enter_page3(context):
    requests.get(normal_url3)


@then(u'the img protected 2 page will show an image')
def check2(context):
    context.response = requests.get(normal_url3)
    assert context.response.status_code == 200


@given(u'enter the malicious image-loader page')
def enter_page_malicious(context):
    context.response = requests.get(malicious_url)


@then(u'the img page will show popup alert')
def check_popup_alert_img1(context):
    response = context.response
    assert malicious in response.text
    context.driver = Chrome()
    context.driver.get(malicious_url)
    alert = context.driver.switch_to.alert
    assert alert is not None, "Popup alert is not shown"
    alert.accept()
    time.sleep(1)


@given(u'enter the malicious img-loader-protected page')
def enter_page_malicious2(context):
    context.response = requests.get(malicious_url2)


@then(u'the img protected page should show popup alert')
def check_popup_alert_img2(context):
    response = context.response
    assert malicious in response.text
    context.driver = Chrome()
    context.driver.get(malicious_url2)
    alert = context.driver.switch_to.alert
    assert alert is not None, "Popup alert is not shown"
    alert.accept()
    time.sleep(1)


@given(u'enter the malicious img-loader-protected2 page')
def enter_page_malicious3(context):
    context.response = requests.get(malicious_url3)


@then(u'the img protected page 2 should show popup alert')
def check_popup_alert_img3(context):
    response = context.response
    assert malicious in response.text
    context.driver = Chrome()
    context.driver.get(malicious_url3)
    alert = context.driver.switch_to.alert
    assert alert is not None, "Popup alert is not shown"
    alert.accept()
    time.sleep(1)
