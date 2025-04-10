
Feature: User cas access sign in

  Scenario: User after logged out can access to sign in
    Given Open target main page
    When Click Sign In
    And  Navigate to side menu and click Sign In
   Then Verify Sign In form opened
