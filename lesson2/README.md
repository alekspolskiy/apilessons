# Count clicks project
This app working wuth https://bitly.com/ api. You may shorten any link and count how much clicks was at this link for all time.

## Installing
[git](https://git-scm.com/doc) must be installed .
Download this folder using:
```
git clone https://github.com/alekspolskiy/apilessons.git
```
Recommended to use [virtualenv/venv](https://docs.python.org/3/library/venv.html)
Python3 must be installed.
Use `pip` or `pip3` for installing requirements:
```
pip install -r requirements.txt
```

## Usage 
For run programm open folder with project in terminal and use: 
``` 
python3 main.py {your link}
```

## Working example

Input:
```
python3 main.py https://dvmn.org/
```
Output:
```
bit.ly/36cIQZ5
```
Input:
```
python3 main.py bit.ly/36cIQZ5
```
Output:
```
2
```
