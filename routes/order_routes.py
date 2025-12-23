from fastapi import APIRouter

"""CREATE ROUTER"""
order_router = APIRouter(prefix="/pedidos", tags=["pedidos"])


@order_router.get("/")
async def get_orders():
    """Rota para pedidos"""
    return {"mensage": "acessou a rota de pedidos"}
