Feature: Testing the echo redirect and redirected-protected files

  Scenario: Testing the functionality for file redirect.php
     Given enter the redirect page
     Then the page will show "Click here to redirect"

 Scenario: Testing the malicious for file redirect.php
     Given enter the malicious redirect page
     Then the redirect page will show popup alert

 Scenario: Testing the functionality for file redirect-protected.php
     Given enter the redirect-protected page
     Then the page will show "Click here to redirect"

 Scenario: Testing the malicious for file redirect-protected.php
     Given enter the malicious redirect-protected page
     Then the redirect malicious page will show popup alert


