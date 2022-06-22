import time

from behave import *
from pageobjects.SignUp import SignUp


@given('User is on "{home}" Page.')
def step_impl(context, home):
    var = SignUp(context).go_to(home)
    assert var, "The user is not navigated to " + home + " screen."


@when("the user provide email and hit Join Now button.")
def step_impl(context):
    SignUp(context).sign_up()


@then("the user gets {email_sms} from Mailosaur server.")
def step_impl(context, email_sms):
    SignUp(context).getEmailVerificationLink(email_sms)


@step("the user fills the onboarding form.")
def step_impl(context):
    SignUp(context).onboarding()


@step("the user gets {sms} from Mailosaur server")
def step_impl(context, sms):
    SignUp(context).getSMSOtpCode(sms)