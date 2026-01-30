from fastapi import APIRouter, Depends

from main import bycrypt_context
from models.model_db import Usuario
from utils.session_db import get_session

"""CREATE ROUTER"""
auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.get("/")
async def get_auth():
    """Rota para autenticação"""
    return {"mensage": "acessou a rota de autenticação", "autenticado": False}


@auth_router.post("/create_user")
async def create_user(
    email: str, password: str, name: str, session=Depends(get_session)
):
    """Rota para criar um usuário"""

    user = session.query(Usuario).filter(Usuario.email == email).first()
    if user:
        return {"mensage": "Já existe um usuário com esse email cadastrado"}
    else:
        password_crypt = bycrypt_context.hash(password)
        new_user = Usuario(nome=name, email=email, senha=password_crypt)
        session.add(new_user)
        session.commit()
        return {"mensage": "Usuário cadastrado com sucesso"}
