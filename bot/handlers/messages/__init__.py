from .ca import router as ca_router
from .drago_price import router as drago_price_router
from .info import router as info_router
from .links import router as links_router
from .new_post import router as new_post_router
from .price import router as price_router
from .website import router as website_router

__all__ = [
    "ca_router",
    "price_router",
    "info_router",
    "new_post_router",
    "website_router",
    "links_router",
    "drago_price_router",
]