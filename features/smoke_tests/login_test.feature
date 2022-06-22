Feature: Sign In

  @login_test
  Scenario: SignIn a user
    Given User is on "LogIn" page to signin.
    When the user provide email and hit Login Now button.
#    Then the user gets email from Mailosaur server.
    Then the user gets sms from Mailosaur server1
        And the user creates the stripe.