# Documentação da API FastAPI

## Descrição Geral

Esta API, construída com o FastAPI, possui dois endpoints. Um para criar um novo item (`POST /items/`) e outro para obter um item existente por ID (`GET /items/{item_id}`). A classe `Item` é um modelo Pydantic que valida os dados de entrada. A lista `items_db` atua como um banco de dados simulado para armazenar os itens. 

## Endpoints

### `POST /items/`

Este endpoint aceita dados de um novo item a ser adicionado ao banco de dados.

#### Parâmetros

- `item`: Um objeto que contém os seguintes campos:
  - `name`: string - O nome do item.
  - `description`: string - A descrição do item.

#### Exemplo de uso

```
curl -X POST "http://localhost:8000/items/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"name\":\"foo\",\"description\":\"A foo item\"}"
```

### `GET /items/{item_id}`

Este endpoint retorna o item com o id especificado.

#### Parâmetros

- `item_id`: integer - O ID do item a ser recuperado.

#### Exemplo de uso

```
curl -X GET "http://localhost:8000/items/0" -H  "accept: application/json"
```

## Notas Importantes

- O índice dos itens começa em 0. Portanto, se você tem 3 itens, os IDs válidos serão 0, 1 e 2.
- Se um ID de item inválido for fornecido para o endpoint `GET /items/{item_id}`, um erro 404 será retornado.

## Dependências Necessárias

- FastAPI: Um moderno e rápido (alto desempenho) framework web para construção de APIs com Python 3.6+ baseado nos padrões para APIs, incluindo JSON Schema, OAuth2, OpenAPI3 e HTTP/2.
- Pydantic: Uma biblioteca para validação de dados e configuração usando Python type annotations.
- Uvicorn: Um servidor ASGI super rápido, para hospedar sua aplicação FastAPI.