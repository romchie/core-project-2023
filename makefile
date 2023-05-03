.SILENT :

run : login.py .credentials
	python3 login.py

.credentials :
	python3 getUserPass.py

resetcredentials : .credentials
	rm -f .credentials
	make .credentials

installrequirements : requirements.txt
	pip3 install -r requirements.txt

reinstallrequirements : requirements.txt
	pip3 uninstall -r requirements.txt
	make installrequirements

clean : 
	rm -f .credentials