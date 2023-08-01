# -- FILE: features/echo_name.feature
Feature: Testing the echo name files

  Scenario: Testing the functionality for file echo-name.php
     Given enter the echo-name page
     Then the page will show "Welcome husam!"

  Scenario: Testing the xss vulnerability for file echo-name.php
     Given enter the malicious link to echo-name page
     Then the page will show popup alert

  Scenario: Testing the functionality for file echo-name-protected.php
     Given enter the echo-name-protected page
     Then the page should show "Welcome husam!"

  Scenario: Testing the xss vulnerability for file echo-name-protected.php
     Given enter the malicious link to echo-name-protected page
     Then the page should show popup alert
