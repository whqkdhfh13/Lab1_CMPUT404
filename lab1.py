import requests
""" For virtualenv "v1", python script used was, in cli, type the following:

py -c "import requests as r; print(r.__version__)"

"""

# print(requests.__version__)
print(requests.get('http://google.com/').text)
