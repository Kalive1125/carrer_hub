
# Carre Hub

Uma breve descrição sobre o que esse projeto faz e para quem ele é


## Documentação

[Pré-Requisitos](#Pré-Requisitos)

[Instalação](#Instalação)


## Pré-Requisitos

Python 3.13
Git


## Instalação


Clone o projeto na sua maquina e entre a raiz do projeto
```bash
git clone git@github.com:guimaraesfe1/carrer_hub.git
cd carrer_hub
```

Instale as dependencias descritas no arquivo pyproject.toml utilizando seu gerenciador de pacotes. Nesse projeto foi utilizado o poetry
```bash
poetry install
```

Ative o ambiente virutal do projeto no linux
```bash
eval $(poetry env activate)
```
No windows
```pwsh
Invoke-Expression (poetry env activate --path)
```

para rodar o servidor de desenvolvimento
```bash
task dev
```