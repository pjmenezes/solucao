![GitHub](https://img.shields.io/github/license/pjmenezes/solucao-calcomp)

# Desafio Técnico - Desenvolvedor de Software - Tarefa 1

## Etapa 1

1. Instale [Mobdus](https://www.modbusdriver.com/diagslave.html)
2. Descompactue o arquivo
3. Abra a pasta
   ```bash
   cd /diagslave-3.4
   ```
4. Liste a pasta

```bash
   ls
```

5. Perceba que existem 4 subpastas, são elas:

- **aarch64-linux-gnu**
- **arm-linux-gnueabihf**
- **i686-linux-gnu**
- **x86_64-linux-gnu**

6. Certifique-se em escolher de acordo com sua processador. No meu caso estarei utilizando **x86_64-linux-gnu**
7. Vou abrir a pasta

```bash
  cd /x86_64-linux-gnu
```

8. Liste a pasta

```bash
   ls
```

9. Perceba que existem 1 arquivo executável chamado:

- **diagslave**

10. Rode esste arquivo utilizando a porta de sua preferência, neste exemplo vou utilizar a porta `502`

```bash
   sudo ./diagslave -m tcp -p 502
```

12. Deixei em execução, este será seu servidor.

## Etapa dois

#### Antes de prosseguir, certifique-se que possui os seguintes:

- **Python3**.
  Se ainda não possui faça o [Download](https://www.python.org/downloads/)
- **Python Pip**. Este é um instalador de pacotes para Python.
  Se ainda não tem instalado, aprenda a instalar [aqui](https://linuxize.com/post/how-to-install-pip-on-ubuntu-20.04/)

13. Execute o comando abaixo dentro da pasta que esta o arquivo do códico.

```bash
   python3 modbus-read-regsiter.py
```

14. Ele criará uma série de dados que possuem informações como: datas, horas e um objeto que foi atibuido o valor inicial de 0; Ele possui dez indices. Veja o exemplo abaixo:

```bash
{"datetime": "2022-07-26T00:26:19.803644", "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
{"datetime": "2022-07-26T00:26:24.806425", "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
{"datetime": "2022-07-26T00:26:29.809971", "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
{"datetime": "2022-07-26T00:26:34.814007", "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
{"datetime": "2022-07-26T00:26:39.817855", "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
```

15. Deixe em execução

16. Na mesma pasta o arquivo e Em uma outra janela do terminal, corra o seguinte comando

```bash
  python3 modbus-write-register.py
```
17. O resultado
```bash
{"datetime": "2022-07-26T01:15:52.585842", "data": [35, 27, 35, 28, 29, 28, 33, 32, 30, 33]}
{"datetime": "2022-07-26T01:15:57.589900", "data": [25, 31, 28, 35, 32, 26, 28, 29, 27, 28]}
{"datetime": "2022-07-26T01:16:02.594950", "data": [31, 33, 28, 30, 27, 27, 28, 34, 27, 32]}
{"datetime": "2022-07-26T01:16:07.597832", "data": [29, 25, 27, 35, 29, 30, 29, 25, 29, 26]}
{"datetime": "2022-07-26T01:16:12.602034", "data": [30, 27, 32, 26, 31, 26, 31, 34, 29, 35]}
{"datetime": "2022-07-26T01:16:17.607494", "data": [25, 26, 33, 34, 33, 31, 29, 31, 35, 28]}
{"datetime": "2022-07-26T01:16:22.610972", "data": [35, 35, 30, 26, 29, 27, 35, 26, 29, 33]}
{"datetime": "2022-07-26T01:16:27.614089", "data": [33, 27, 33, 29, 28, 28, 29, 32, 28, 31]}
```
18. Dentro da pasta que seus código estão, será criado automaticamente um arquivo em formato `txt`, e enquanto o código estiver em execução, o arquivo `txt` atualizará automticamente


### Para visualizar a execução clique no gif abaixo e assista no Youtube.
[![HTML5 e CSS3 - One Page Site](https://media.giphy.com/media/hHjOpLaawe5rvWvcTn/giphy.gif)](https://youtu.be/ou07jE9Fe48 "Assistir no YouTube")
