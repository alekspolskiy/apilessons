# Space Instagram
This project downloads Hubble and SpaceX images and uploads it to instagram account.

## How to install
Use [dotenv](https://pypi.org/project/python-dotenv/) to import your login and password into project.

 `
 .env
 `
:
```
INSTA_LOGIN='{your login}'
INSTA_PASSWORD='{your password}'
```
Recommended to use [virtualenv/venv](https://docs.python.org/3/library/venv.html).
Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
For run app use:
```
python3 main.py
```
## Project Goals
The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).