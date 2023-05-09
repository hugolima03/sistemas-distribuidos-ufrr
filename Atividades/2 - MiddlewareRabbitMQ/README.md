# Para executar a atividade

```
# Iniciar o RabbitMQ server utilizando docker
docker compose up

# Instalar os pacotes
pip install pika
pip install psutil
pip install playsound

# Executar os receivers
python3 cpu-temp-receive.py
python3 fire-event-receive.py

# Executar o script que envia a temperatura a cada 5 segundos
python3 send.py
```