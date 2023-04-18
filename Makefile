install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:	
	black *.py dblib/*py

all: install format