import time

from behave import *
from pageobjects.LogIn import LogIn


@given('User is on "{login}" page to signin.')
def step_impl(context, login):
    var = LogIn(context).go_to(login)
    assert var, "The user is not navigated to " + login + " screen."


@when("the user provide email and hit Login Now button.")
def step_impl(context):
    LogIn(context).sign_in()


@step("the user gets {sms} from Mailosaur server1")
def step_impl(context, sms):
    LogIn(context).getSMSOtpCode(sms)


@step("the user creates the stripe.")
def step_impl(context):
    LogIn(context).onboarding()
