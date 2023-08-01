import time
import requests
from selenium import webdriver
from behave import *
from selenium.common.exceptions import TimeoutException

target = "husam"
malicious = "'/><script>alert('hello hacker')</script>"
url1 = "http://localhost/Assignment3/redirect.php?target="
url2 = "http://localhost/Assignment3/redirect-protected.php?target="
normal_url1 = url1+target
normal_url2 = url2+target

malicious_url = url1 + malicious
malicious_url2 = url2 + malicious


@given(u'enter the redirect page')
def enter_page(context):
    requests.get(normal_url1)


@then(u'the page will show "Click here to redirect"')
def check(context):
    response = requests.get(normal_url1)
    print(response.text)
    assert "redirect" in response.text


@given(u'enter the malicious redirect page')
def enter_page(context):
    requests.get(malicious_url)


@then(u'the redirect page will show popup alert')
def check_popup_alert(context):
    response = requests.get(malicious_url)
    print(response.text)
    assert malicious in response.text
    context.driver = webdriver.Chrome()
    context.driver.get(malicious_url)
    alert = context.driver.switch_to.alert
    assert alert is not None, "Popup alert is not shown"
    alert.accept()
    time.sleep(1)


@given(u'enter the redirect-protected page')
def enter_page(context):
    requests.get(normal_url2)


@given(u'enter the malicious redirect-protected page')
def enter_page(context):
    requests.get(malicious_url2)


@then(u'the redirect malicious page will show popup alert')
def check_popup_alert(context):
    response = requests.get(malicious_url2)
    print(response.text)
    assert malicious in response.text
    context.driver = webdriver.Chrome()
    context.driver.get(malicious_url2)
    alert = context.driver.switch_to.alert
    assert alert is not None, "Popup alert is not shown"
    alert.accept()
    time.sleep(1)
