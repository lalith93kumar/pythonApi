sudo -H pip install -U pipenv
pipenv install --dev
pip install allure-pytest-bdd
pytest tests/config.py -v -s --alluredir=allure_result_folder