Feature: Navigation from Dashboard to All Reviewers
  As a user
  I want to navigate from the dashboard to the "All Reviewers" page
  So that I can see the list of all reviewers

  Scenario: User clicks the "View All Reviewers" button
    Given the user is on the dashboard page
    When the user clicks the "View All Reviewers" button
    Then the user is redirected to the "All Reviewers" page
    And the "All Reviewers" page displays a table of reviewers