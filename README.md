# CoRE Class Project Spring 2023
A Python script that reads in your Binghamton University PODS username and password via stdin and signs you in to Brightspace on Chrome. If your inputted username and password are legitimate, you will be prompted to enter your 2FA code via stdin. You will then be logged in to your Brightspace page. Your username and password are stored in a hidden file which can be manually overwritten or cleared at any time. Your PODS username and password are only stored in the local directory of the program.
### Important Notes
- please verify that Chrome is installed and up to date
- program tested locally and works on OSX (unsure about other builds)

### Documentation
Install necessary requirements (webscraping tools)  
```$ make installrequirements``` (NOTE: you may also want to try `$ make reinstallrequirements`)  

Run the program  
```$ make```

Reset the stored `username` and `password`  
```$ make resetcredentials```

Clear the stored `username` and `password`  
```$ make clean```