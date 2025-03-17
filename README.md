# SMS Application for testing
This is a small SMS application, built with python (bottle) and nginx.

1.) Built with python (bottle). \
2.) Nginx webserver \
3.) Webpage/form (HTML) \
4.) Systemd unit file to enable on startup

## File structure
```
sms_application/
├── sms_app.py       # python Bottle application
├── index.html       # html form for sending SMS
├── nginx/
│   └── sms_app.conf   # nginx configuration file
└── systemd/
    └── sms_app.service # systemd unit service file
```

## Importan Notes
* Remember to replace the variable YOUR_IP_HERE in the `sms_app.conf` file with an actual IP or domain
* Currently the application is using environment variables to store the credentials for testing purposes. Working on a more secure method (python secrets)
* Make sure to update the information in the systemd unit file and set correct permissions

