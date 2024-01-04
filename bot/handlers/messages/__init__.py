from .ca import router as ca_router
from .price import router as price_router
from .info import router as info_router
from .new_post import router as new_post_router

__all__ = [
    "ca_router",
    "price_router",
    "info_router",
    "new_post_router",
]