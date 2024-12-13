Feature: Contact Page Functionality
  As a user
  I want to view the contact information
  So that I can send messages to the listed contacts

  Scenario: Viewing and interacting with contacts on the Contact page
    Given the user is on the Contact page
    Then the user sees a list of contact cards with names, emails, and message buttons
    When the user clicks the "Message" button for a contact
    Then the email client opens with the correct email address pre-filled