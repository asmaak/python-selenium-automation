Feature: Target navigate to sign in page
  # Enter feature description here

  Scenario: user can navigate to Sign In
    Given Open target main page
    When Click Sign In
    And  click Sign In side menu
    Then Verify Sign In form opened