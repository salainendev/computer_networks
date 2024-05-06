### Перед запуском:
#### установить ngrok по инструкции с сайта
``` shell
curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc \
	| sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null \
	&& echo "deb https://ngrok-agent.s3.amazonaws.com buster main" \
	| sudo tee /etc/apt/sources.list.d/ngrok.list \
	&& sudo apt update \
	&& sudo apt install ngrok
ngrok config add-authtoken <ваш токен с сайта ngrok , там надо зарегаться>
```
#### установить докер-образы (я надеюсь докер у вас есть)
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
