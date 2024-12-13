Feature: User Signup

  Scenario: Successful signup with valid data
    Given I am on the signup page
    When I fill in "email" with "testuser@example.com"
    And I fill in "username" with "testuser"
    And I fill in "password" with "password123"
    And I check the terms and conditions
    And I click on "Sign Up"
    Then I should see "Account created successfully!"

  Scenario: Signup with an existing username
    Given I am on the signup page
    When I fill in "email" with "newuser@example.com"
    And I fill in "username" with "testuser"
    And I fill in "password" with "password123"
    And I check the terms and conditions
    And I click on "Sign Up"
    Then I should see "Username already exists"

  Scenario: Signup with an existing email
    Given I am on the signup page
    When I fill in "email" with "testuser@example.com"
    And I fill in "username" with "newuser"
    And I fill in "password" with "password123"
    And I check the terms and conditions
    And I click on "Sign Up"
    Then I should see "Email already registered"
