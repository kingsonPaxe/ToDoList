# TesteComFastAPI

Este projeto é uma aplicação backend desenvolvida utilizando o framework FastAPI. O objetivo do projeto é fornecer uma API rápida e eficiente para gerenciar dados de uma aplicação Android.

## Bibliotecas Utilizadas

- **FastAPI**: Um framework web moderno e rápido para construir APIs com Python 3.6+ baseado em padrões como OpenAPI e JSON Schema.
- **Uvicorn**: Um servidor ASGI rápido e leve, usado para servir a aplicação FastAPI.


## Estrutura do Projeto

- **app**: Contém o código principal da aplicação FastAPI.
    - **main.py**: O ponto de entrada da aplicação.
    - **models.py**: Define os modelos de dados utilizando SQLAlchemy.
    - **schemas.py**: Define os esquemas de dados utilizando Pydantic.
    - **crud.py**: Contém as operações CRUD (Create, Read, Update, Delete) para interagir com o banco de dados.
    - **database.py**: Configuração da conexão com o banco de dados.
    - **routers**: Contém os diferentes endpoints da API organizados por funcionalidade.
- **tests**: Contém os testes automatizados para a aplicação.

## Como Executar

1. Clone o repositório.
2. Instale as dependências utilizando `pip install -r requirements.txt`.
3. Execute a aplicação com `uvicorn app.main:app --reload`.
4. Acesse a documentação interativa da API em `http://127.0.0.1:8000/docs`.

## Contribuição

Sinta-se à vontade para contribuir com o projeto através de pull requests. Certifique-se de que todas as alterações sejam acompanhadas de testes apropriados.