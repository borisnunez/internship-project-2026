# Created by borisnunez at 6/5/26
Feature: Tests for registration page

  Scenario: The user can enter the information into the input fields on the registration page
    Given Open the registration page
    When The user enters "John Smith" in the First and Last Name field
    And User enters "8889997777" in the phone number field
    And The user enters "john.smith@example.com" in the email field
    And The user enters "Mypassword123&" in the password field
    And User enters "testcompany.com" in the company website field
    Then Verify first and last name field contains "John Smith"
    And Verify phone number field should contain "8889997777"
    And Verify email field should contain "john.smith@example.com"
    And Verify password field should contain "Mypassword123&"
    And Verify company website field should contain "testcompany.com"