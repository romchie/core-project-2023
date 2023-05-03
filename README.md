# CoRE Class Spring 2023
A Python script that reads in your Binghamton PODS username and password via stdin and signs you in to Brightspace on Chrome

### Important Notes
- make sure Chrome is installed and up to date
- works locally on OSX (unsure about other builds)

### Documentation
Install necessary requirements (webscraping tools)  
```$ make installrequirements``` (NOTE: you may also want to try `$ make reinstallrequirements`)  

Run the program  
```$ make```

Reset the stored `username` and `password`  
```$ make resetcredentials```

Clear the stored `username` and `password`  
```$ make clean```