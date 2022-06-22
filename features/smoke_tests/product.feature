Feature: Sign In

  @product
    @login
  Scenario: Product addition
      Given User is on "Product" after signin.
    When the user provide email and hit Login's button.
#    Then the user gets email from Mailosaur server.
    Then the user gets sms from Mailosaur server1
        And the user creates the dashboard.