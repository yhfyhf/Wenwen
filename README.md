## Wenwen
A Q&A forum like Quora and Zhihu.

## Deploy

### Generate SSL Certifate 

	openssl genrsa 1024 > host.key
	chmod 400 host.key
	openssl req -new -x509 -nodes -sha1 -days 365 -key host.key > host.crt

### Set up Environment

	virtualenv app
	cd app
	source bin/activate
	git clone https://github.com/yhfyhf/Wenwen mysite
	cd mysite
	pip install -r requirements.txt -i http://pypi.douban.com/simple

### Change PYTHONPATH

	echo "export PYTHONPATH=your/path/to/app:\$PYTHONPATH" >> bin/activate

### Run

	python runserver.py
	