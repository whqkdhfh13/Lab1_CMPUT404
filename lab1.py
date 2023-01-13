import requests
""" For virtualenv "v1", python script used was, in cli, type the following:

py -c "import requests as r; print(r.__version__)"

"""

# print(requests.__version__)
url_google = 'http://google.com/'
url_myscript = 'https://raw.githubusercontent.com/whqkdhfh13/Lab1_CMPUT404/main/lab1.py'
url_to_use = url_myscript

print(requests.get(url_myscript).text)
