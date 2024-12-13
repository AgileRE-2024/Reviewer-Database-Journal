Feature: Upload Paper Manuscript
  As a user, I want to upload a manuscript and find recommended reviewers.

  Scenario: User submits a manuscript form
    Given the user is on the upload manuscript page
    When the user fills the form with valid data
    And the user agrees to the terms and conditions
    And the user submits the form
    Then the user is redirected to the recommendation page
    And the system displays reviewer recommendations

  Scenario: User submits a manuscript form with incomplete fields
    Given the user is on the upload manuscript page
    When the user leaves the "journal-title" field empty
    And the user fills the "abstract" field with valid data
    And the user agrees to the terms and conditions
    And the user submits the form
    Then a JavaScript alert appears with the message "Please fill out this field"