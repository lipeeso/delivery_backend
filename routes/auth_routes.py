from fastapi import APIRouter

"""CREATE ROUTER"""
auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.get("/")
async def get_auth():
    """Rota para autenticação"""
    return {"mensage": "acessou a rota de autenticação", "autenticado": False}
