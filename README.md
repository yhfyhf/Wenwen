## 问问
一个类似于 Quora, Zhihu 的知识社区。

## 安装步骤

### 生成自签名的 SSL 证书 

	openssl genrsa 1024 > host.key
	chmod 400 host.key
	openssl req -new -x509 -nodes -sha1 -days 365 -key host.key > host.crt

### 配置环境

	virtualenv app
	cd app
	source bin/activate
	git clone https://github.com/yhfyhf/Wenwen mysite
	cd mysite
	pip install -r requirements.txt -i http://pypi.douban.com/simple

### 修改 PYTHONPATH

	echo "export PYTHONPATH=your/path/to/app:\$PYTHONPATH" >> bin/activate

### 运行

	python runserver.py
	