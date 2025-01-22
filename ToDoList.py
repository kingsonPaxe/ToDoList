from fastapi import FastAPI 
from typing import Optional
app = FastAPI()

tarefas = [
    {
        "nome": "Jeovani Paxe",
        "Descrição": "Varrer o quintal",
        "Status": False
     
    },

    {
        "nome": "Maria Paxe",
        "Descrição": "Lavar a louça",
        "Status": False
     
    },

    {
        "nome": "Angela Paxe",
        "Descrição": "Fazer compras",
        "Status": False
     
    },
]

# Criando a rota home...

@app.get("/")
def home():
    return tarefas

# Pegando cada ID
@app.get("/tarefa/{task_id}")
def take_task(task_id:int):
    return tarefas[task_id-1]

#Apagando um elemento no nosso api
@app.delete("/tarefa/apagar/{task_id}")
def delete_tasks(task_id:int): 
        return tarefas.pop(task_id-1)

# Criar a tarefa, ou seja fazendo o post

@app.post("/tarefa/atualizar/{task_id}")
def create_tasks(nome:str, descrição:str,status: bool):
    tarefas.append({
        "nome": nome,
        "Descrição": descrição,
        "Status": status
    })


# Fazer o Update
@app.put("/tarefa/{task_id}")
def update_task(task_id: int, nome: Optional[str] = None, descrição: Optional[str] = None, status: Optional[bool] = None):
    if nome is not None:
        tarefas[task_id-1]["nome"] = nome
    if descrição is not None:
        tarefas[task_id-1]["Descrição"] = descrição
    if status is not None:
        tarefas[task_id-1]["Status"] = status
    return tarefas[task_id-1]
