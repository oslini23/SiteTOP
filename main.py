from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "API do Marketplace de Sites"}

@app.get("/api/sites")
def get_sites():
    return [
        {"id": 1, "titulo": "Site de Notícias", "preco": "R$ 3.000"},
        {"id": 2, "titulo": "Loja Virtual de Roupas", "preco": "R$ 7.500"}
    ]
