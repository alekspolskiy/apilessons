#Space Instagram
This project downloads Hubble and SpaceX images and uploads it to instagram account.

##How to install
Use [dotenv](https://pypi.org/project/python-dotenv/) to import your login and password into project.
 .env:
```
LOGIN='{your login}'
PASSWORD='{your password}
```
main.py:
```
from dotenv import load_dotenv

load_dotenv('.env')
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')

load_photo(login, password)
```
Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
##Project Goals
The code is written for educational purposes on online-course for web-developers dvmn.org.