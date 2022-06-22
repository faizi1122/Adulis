Feature: Sign Up

  @smoke_test
  Scenario: Register as a new user
    Given User is on "SignUp" page.
    When the user provide email and hit Join Now button.
    Then the user gets email from Mailosaur server.
    And the user fills the onboarding form.
    And the user gets sms from Mailosaur server
