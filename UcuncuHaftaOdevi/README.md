# Installs

```
sudo apt update
```

```
sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools
```

```
pip install gunicorn flask requests
```

# Setup

```
sudo nano /etc/systemd/system/nobelApi.service
```

## Gunicorn Yapılandırmaları

### nobelApi.service 

```
[Unit]
Description=Gunicorn instance to serve nobelApi
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/Acik-Kaynak-Yazilim/UcuncuHaftaOdevi
Environment="PATH=/home/ubuntu/Acik-Kaynak-Yazilim/UcuncuHaftaOdevi/nobelApienv/bin"
ExecStart=/home/ubuntu/Acik-Kaynak-Yazilim/UcuncuHaftaOdevi/nobelApienv/bin --workers 3 --bind unix:nobelApi.sock -m 007 wsgi:app

[Install]
WantedBy=multi-user.target
```

### systemctl i başlatma

```
sudo systemctl start myproject
sudo systemctl enable myproject
```

```
sudo systemctl status myproject
```

### çıktı buna benzer olmalı

```
● myproject.service - Gunicorn instance to serve myproject
     Loaded: loaded (/etc/systemd/system/myproject.service; enabled; vendor preset: enabled)
     Active: active (running) since Tue 2022-05-10 19:40:41 UTC; 9s ago
   Main PID: 17300 (gunicorn)
      Tasks: 4 (limit: 2327)
     Memory: 56.0M
        CPU: 514ms
     CGroup: /system.slice/myproject.service
             ├─17300 /home/sammy/myproject/myprojectenv/bin/python3 /home/sammy/myproject/myprojectenv/bin/gunicorn --workers 3 --bind unix:myproject.sock -m 007 wsgi:app
             ├─17301 /home/sammy/myproject/myprojectenv/bin/python3 /home/sammy/myproject/myprojectenv/bin/gunicorn --workers 3 --bind unix:myproject.sock -m 007 wsgi:app
             ├─17302 /home/sammy/myproject/myprojectenv/bin/python3 /home/sammy/myproject/myprojectenv/bin/gunicorn --workers 3 --bind unix:myproject.sock -m 007 wsgi:app
             └─17303 /home/sammy/myproject/myprojectenv/bin/python3 /home/sammy/myproject/myprojectenv/bin/gunicorn --workers 3 --bind unix:myproject.sock -m 007 wsgi:app

May 10 19:40:41 r systemd[1]: Started Gunicorn instance to serve myproject.
. . .
```
## Nginx Yapılandırmaları

```
sudo nano /etc/nginx/sites-available/nobelApi
```

```
server {
    listen 80;
    server_name 198.162.1.100; 

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/Acik-Kaynak-Yazilim/UcuncuHaftaOdevi;
    }
}
```

### Yapılandırmayı etkinleştirmek
```
sudo ln -s /etc/nginx/sites-available/nobelApi /etc/nginx/sites-enabled
```

### Bu dizindeki dosyayla sözdizimi hatalarını test edebilirsiniz:
```
sudo nginx -t
```
### nginx i yeniden başlatma
```
sudo systemctl restart nginx
```

### Son olarak güvenlik duvarı ayarları

```
sudo ufw delete allow 5000
sudo ufw allow 'Nginx Full'
```
