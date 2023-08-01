import time
import requests
from selenium import webdriver
from behave import *
from selenium.common.exceptions import TimeoutException

name = "husam"
malicious1 = "/'><script>alert('Hey hacker')</script>"

malicious2 = '/"><script>alert("Hey hacker")</script>'
url1 = "http://localhost/Assignment3/echo-attr.php?name="
url2 = "http://localhost/Assignment3/echo-attr2.php?name="


normal_url1 = url1 + name
normal_url2 = url2 + name

malicious_url_att11 = url1 + malicious1
malicious_url_att12 = url1 + malicious2

malicious_url_att21 = url2 + malicious1
malicious_url_att22 = url2 + malicious2


        ### First scenario ####

@Given(u'enter the echo-attr page')
def enter_page(context):
    requests.get(normal_url1)


@then(u'the page will show "Welcome user!"')
def check(context):
    response = requests.get(normal_url1)
    assert "user" in response.text

    ### second scenario ####


@Given(u'enter the malicious echo-attr page')
def enter_malicious_page(context):
    requests.get(malicious_url_att11)


@then(u'the attr page will show popup alert')
def check_popup_alert(context):
    response = requests.get(malicious_url_att11)
    assert malicious1 in response.text
    context.driver = webdriver.Chrome()
    context.driver.get(malicious_url_att11)
    time.sleep(1)
    alert = context.driver.switch_to.alert
    assert alert is not None, "Popup alert is not shown"
    alert.accept()

########## echo attr2 ###########

    ### First scenario ####


@Given(u'enter the echo-attr2 page')
def enter_page(context):
    requests.get(normal_url2)


@then(u'the page should show "Welcome user!"')
def check_protected_page(context):
    response = requests.get(normal_url2)
    assert "user" in response.text

    ### Second scenario ####


@Given(u'enter the /> malicious echo-attr2 page')
def enter_malicious_protected_page(context):
    requests.get(malicious_url_att22)


@then(u'the protected page should show popup alert')
def check_popup_allert2(context):
    response22 = requests.get(malicious_url_att22)
    assert malicious2 in response22.text, response22.text
    context.driver = webdriver.Chrome()
    context.driver.get(malicious_url_att22)
    time.sleep(1)
    alert = context.driver.switch_to.alert
    assert alert is not None, "Popup alert is not shown"
    alert.accept()
