# Programming vacancies compare
This project gets information about vacancies from [hh](https://hh.ru/) and [SuperJob](https://www.superjob.ru/).

## How to install
Use [dotenv](https://pypi.org/project/python-dotenv/) to import your secret key into project. You have to register your app [here](https://api.superjob.ru/register).

 `
 .env
 `
:
```
SUPERJOB_SECRET_KEY='your_key'
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