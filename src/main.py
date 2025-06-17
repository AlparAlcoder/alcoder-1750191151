Desculpe, mas parece haver um erro na sua solicitação. Você mencionou "gere uma api em nodejs com dois endpoints", mas pediu um código Python usando FastAPI e Pydantic. Como devo proceder? Você gostaria de uma API Python ou NodeJS? 

Como sua solicitação original é para um código Python usando FastAPI e Pydantic, aqui está um exemplo de como poderia ser essa API com dois endpoints:


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str

items_db = []

@app.post("/items/")
async def create_item(item: Item):
    items_db.append(item)
    return item

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id >= len(items_db):
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]


Neste código, a API FastAPI possui dois endpoints: um para criar um novo item (POST /items/) e outro para obter um item existente por ID (GET /items/{item_id}). A classe Item é um modelo Pydantic que valida os dados de entrada. A lista items_db atua como um banco de dados simulado para armazenar os itens. O tratamento de erro é fornecido pelo HTTPException, que retorna um erro 404 se um item solicitado não for encontrado.