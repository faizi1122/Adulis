import time

from behave import *
from pageobjects.LogIn import LogIn
from pageobjects.Product import Product


@given('User is on "{login}" after signin.')
def step_impl(context, login):
    var = LogIn(context).go_to(login)
    assert var, "The user is not navigated to " + login + " screen."


@when("the user provide email and hit Login's button.")
def step_impl(context):
    LogIn(context).sign_in()


@step("the user gets {sms} from the Mailosaur server")
def step_impl(context, sms):
    LogIn(context).getSMSOtpCode(sms)


@step("the user creates the dashboard.")
def step_impl(context):
    Product(context).product_addition()
