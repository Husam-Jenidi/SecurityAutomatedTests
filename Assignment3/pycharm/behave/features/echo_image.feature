Feature: Testing the image loader files

  Scenario: Testing the functionality for file img-loader.php
     Given enter the img-loader page
     Then the img page will show an image

 Scenario: Testing the malicious for file img-loader.php
     Given enter the malicious image-loader page
     Then the img page will show popup alert

  Scenario: Testing the functionality for file img-loader-protected.php
     Given enter the img-loader-protected page
     Then the img protected page will show an image

  Scenario: Testing the malicious for file img-loader-protected.php
     Given enter the malicious img-loader-protected page
     Then the img protected page should show popup alert

  Scenario: Testing the functionality for file img-loader-protected2.php
     Given enter the img-loader-protected2 page
     Then the img protected 2 page will show an image

  Scenario: Testing the malicious for file img-loader-protected2.php
     Given enter the malicious img-loader-protected2 page
     Then the img protected page 2 should show popup alert
