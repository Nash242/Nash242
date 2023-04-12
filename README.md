created an env
''' conda create -n wineq python=3.7 -y'''

activate env
''' conda activate wineq'''

created a req file

install the requirements
'''pip install -r requirements.txt'''

download the data

git init

dvc init 
'''pip install fsspec==2022.7.1'''

dvc add data_given/winequality.csv

git add .

git commit -m "first commit"

git add . && git commit -m "update README.md"

git remote add origin https://github.com/Nash242/dvc_demo.git

git branch -M main

tox command
'''tox'''

for rebuilding tox
'''tox -r'''

pytest command
'''pytest -v'''

setup commands
''' pip install -e'''

Build your own package commands
'''python setup.py sdist bdist_wheel'''

