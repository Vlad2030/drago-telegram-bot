from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import mapped_column

from core.database import Base


class ExchangesInfoDatabase(Base):
    __tablename__ = "exchanges_info"

    id = mapped_column(Integer, primary_key=True, index=True)
    name = mapped_column(String, nullable=False)
    link = mapped_column(String, nullable=False)
    price = mapped_column(Float, nullable=False, default=0.0)
    price_change = mapped_column(Float, nullable=False, default=0.0)
    price_h24_high = mapped_column(Float, nullable=True, default=0.0)
    price_h24_low = mapped_column(Float, nullable=True, default=0.0)
    h24_volume = mapped_column(Float, nullable=True, default=0.0)
    h24_volume_quote = mapped_column(Float, nullable=True, default=0.0)
