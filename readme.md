sudo yum install git python pip -y
pip install -r ./requirements.txt
pytest tests/config.py -v -s --alluredir=allure_result_folder
allure serve allure_result_folder