
# Phisherman
![MIT License](https://img.shields.io/bower/l/p?style=for-the-badge)

An anti-phishing Discord bot that moderates phishing links sent to the server using data from the PhishTank API. 
[Add](https://discord.com/api/oauth2/authorize?client_id=1076309446831120584&permissions=8&scope=bot) to you server



## [PhishTank API](https://phishtank.org/api_info.php)
The backend calls a request to the current PhishTank database to fetch all phishing links stored on every 24 hours. Everytime a user sends a message Phisherman will scan the local copy of the database for a matching phishing url and delete the message accordingly. 



## Deployment
Bot is currently deployed on a local Raspberry Pi


## Contributing
Contributions are always welcome! Just make a fork of the repo and a pr. Heads up that the number of API calls a day to PhishTank is limited so if the code doesnt work you might need to wait a bit or modify the code to use a local backed up version of the data. 

