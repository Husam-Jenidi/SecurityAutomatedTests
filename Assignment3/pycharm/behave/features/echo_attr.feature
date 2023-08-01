# -- FILE: features/echo_attr.feature

Feature: Testing the echo attr files

    #######file echo_attr#######

  Scenario: Testing the functionality for file echo_attr.php
     Given enter the echo-attr page
     Then the page will show "Welcome user!"

  Scenario: Testing the malicious file echo_attr.php
     Given  enter the malicious echo-attr page
     Then the attr page will show popup alert


    # -- FILE: features/echo_attr2.feature
    #######file echo_attr2#######

  Scenario: Testing the functionality for file echo_attr2.php
     Given enter the echo-attr2 page
     Then the page should show "Welcome user!"



  Scenario: Testing the /> malicious file echo_attr2.php
     Given enter the /> malicious echo-attr2 page
     Then the protected page should show popup alert
