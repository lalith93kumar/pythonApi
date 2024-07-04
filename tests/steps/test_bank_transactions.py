import pytest  
from pytest_bdd import scenarios, scenario, given, when, then  
from ..libs import HandlerFrame
from ..apiClient import createPetEndpoint
import json
# Fixtures  
@pytest.fixture  
def account_balance():  
    return {"balance": 100}  # Using a dictionary to allow modifications  
  
# Given Steps  
@given("the account balance is $100")  
def account_initial_balance(account_balance):  
    payload = {'category' : {'id':'0', 'name' :'string'},'name':'doggie', 'photoUrls':['string'], 'tags' :[{'id' :'0', 'name' :'string'}], 'status' :'available'}
    create = createPetEndpoint.getInstance(payload)
    resp = HandlerFrame.getInstance().request_handler(create)
    resp_body = resp.json()
    assert resp.status_code ==200
    print(resp_body) 
  
# When Steps  
@when("I deposit $20")  
def deposit(account_balance):  
    account_balance["balance"] += 20  
  
# Then Steps  
@then("the account balance should be $120")  
def account_balance_should_be(account_balance):  
    assert account_balance["balance"] == 120