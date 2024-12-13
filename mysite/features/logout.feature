Feature: Logout functionality
  As a user
  I want to log out of the application
  So that my session is securely ended

  Scenario: Logging out successfully
    Given the user is logged into the dashboard
    When the user clicks the "Logout" button
    Then the user is redirected to the login page
    And a success message is displayed