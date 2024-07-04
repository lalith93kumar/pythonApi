import pytest
from pytest_bdd import scenarios

# Load all scenarios from the feature file
scenarios("./createPetsAPI.feature")