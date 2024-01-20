from sqlalchemy import Float, Integer
from sqlalchemy.orm import mapped_column

from core.database import Base


class TotalInfoDatabase(Base):
    __tablename__ = "total_info"

    id = mapped_column(Integer, primary_key=True, index=True)
    price = mapped_column(Float, nullable=False, default=0.0)
    price_change = mapped_column(Float, nullable=False, default=0.0)
    total_h24_volume = mapped_column(Float, nullable=False, default=0.0)
    total_h24_volume_quote = mapped_column(Float, nullable=False, default=0.0)
    total_h24_high = mapped_column(Float, nullable=False, default=0.0)
    total_h24_low = mapped_column(Float, nullable=False, default=0.0)
    total_ath = mapped_column(Float, nullable=False, default=0.3407)
    total_atl = mapped_column(Float, nullable=False, default=0.004090)
