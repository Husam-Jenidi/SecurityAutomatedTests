import time
import requests
from selenium import webdriver
from behave import *
from selenium.common.exceptions import TimeoutException

name = "husam"
malicious = '"/><script>alert("hello")</script>'

url1 = "http://localhost/Assignment3/echo-name.php?name="
normal_url1 = url1 + name
malicious_url1 = url1 + malicious

url2 = "http://localhost/Assignment3/echo-name-protected.php?name="
normal_url2 = url2 + name
malicious_url2 = url2 + malicious


@given(u'enter the echo-name page')
def enter_page(context):
    requests.get(normal_url1)


@then(u'the page will show "Welcome husam!"')
def check(context):
    response = requests.get(normal_url1)
    assert "Welcome husam!" in response.text


@given(u'enter the malicious link to echo-name page')
def enter_malicious_page(context):
    requests.get(malicious_url1)


@then(u'the page will show popup alert')
def check_popup_alert(context):
    response = requests.get(malicious_url1)
    print(response.text)
    assert malicious in response.text
    context.driver = webdriver.Chrome()
    context.driver.get(malicious_url1)
    alert = context.driver.switch_to.alert
    assert alert is not None, "Popup alert is not shown"
    alert.accept()
    time.sleep(1)

########## the second file##############


@given(u'enter the echo-name-protected page')
def enter_protected_page(context):
    requests.get(normal_url2)


@then(u'the page should show "Welcome husam!"')
def check_protected_page(context):
    response = requests.get(normal_url2)
    assert "Welcome husam!" in response.text


@given(u'enter the malicious link to echo-name-protected page')
def enter_malicious_protected_page(context):
    requests.get(malicious_url2)


@then(u'the page should show popup alert')
def check_popup_alert2(context):
    response2 = requests.get(malicious_url2)
    assert malicious in response2.text, response2.text
    context.driver = webdriver.Chrome()
    context.driver.get(malicious_url2)
    alert = context.driver.switch_to.alert
    assert alert is not None, "Popup alert is not shown"
    alert.accept()
    time.sleep(1)
