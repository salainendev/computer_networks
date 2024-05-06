### Перед запуском:
#### установить ngrok по инструкции с сайта
```bash
sudo apt install nginx
docker pull mysql:latest
docker pull wordpress:latest

```

### чтобы поднять вордпресс

```bash
docker compose up
```

### чтобы поднять на localhost
```bash
sudo vim /etc/nginx/sites-enabled/default
```

#### пишем в файле
```bash
server {
        server_name _;
        location / {
                proxy_pass http://localhost:8000;
        }       
}       
```


### перезагружаем nginx
```bash
sudo systemctl restart nginx 
```
### открываем доступ через ngrok
```bash
ngrok http 80
```

#### теперь у нас есть доступ по ссылке
