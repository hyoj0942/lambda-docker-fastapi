from fastapi import APIRouter, Path

router = APIRouter(prefix="/orders", tags=["Orders"])
metadata_order = {"name": "Order API Version 1", "description": "Version 1 ORDER API"}


@router.get(path="", summary="GET Orders")
async def get_orders():
    return {"message": "Get Orders"}


@router.post(path="", summary="POST Orders")
async def register_order():
    return {"message": "Register Order"}


@router.patch(path="/{order_id}", summary="PATCH Orders")
async def update_order(order_id: int = Path(..., title="Order Number")):
    return {"message": f"Update Order by {order_id}"}


@router.delete(path="/{order_id}", summary="DELETE Orders")
async def delete_order(order_id: int = Path(..., title="Order Number")):
    return {"message": f"Delete Order by {order_id}"}