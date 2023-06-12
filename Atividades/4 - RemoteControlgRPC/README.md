# Atividade 4 - Hugo Lima Romão

ATENÇÃO: Para mais praticidade utilize o jupyter notebook para executar os códigos e obter acesso as anotações. Ex: ```jupyter notebook .```

Nesta atividade criamos uma aplicação de controle remoto de uma máquina Linux. O objetivo é permitir que o cliente envie comandos em formato de string para o servidor, que irá executar esses **comandos** em uma máquina Linux e retornar o **resultado** para o cliente.

O primeiro passo é instalar os pacotes utilizados para comunicação RPC.
```pip install grpcio grpcio-tools```

Como todas as interfaces já estão declaradas, resta apenas executar uma instância de servidor e outra de cliente.

Para executar uma instância do servidor: ```python3 server.py```
Para executar uma instância do cliente: ```python3 client.py```

Os usuários cadastrados são listados a seguir, utilize estas credenciais para enviar mensagens.
users = [
    {"name": "Hugo", "password": "RPC"},
    {"name": "Leandro Balico", "password": "ufrr"},
]

Como bônus esta atividade possui recursos de autenticação e um sistema de log, que armazena todos comandos enviados para o servidor no arquivo cmds.txt. Desta forma é possível rastrear o usuário que executou um código malicioso.