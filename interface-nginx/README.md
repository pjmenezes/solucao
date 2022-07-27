
# Tarefa 2 - Interface


1. Criei um arquivo `Dockerﬁle`; dentro deste arquivo estou criando minha própia imagem personalizada com Ubuntu e nginx rodando dentro dele
2. Criei um arquivo do formato html e css
3. Crie as images
   ```bash
   docker build -t interface-nginx .
   ```
4. Coloque o container em execução 
```bash
   docker run -d -p 8080:80 custom-nginx
   ```   
4. Você também pode conferir o arquivo criado que esta dentro do container 

```bash
    docker exec -it  [id do container]  /bin/bash

```
