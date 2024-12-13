Feature: Upload OJS File and Start Scraping
  As a user
  I want to upload an OJS file
  And start scraping reviewers from the uploaded data
  So that I can manage reviewers in the system

  Scenario: Uploading a valid OJS file and starting the scraping process
    Given the user is on the Upload OJS page
    When the user selects a valid OJS file and clicks the upload button
    Then the file is successfully uploaded
    When the user clicks the "Start Scraping" button
    Then the scraping process starts
    And scraping statistics are displayed
