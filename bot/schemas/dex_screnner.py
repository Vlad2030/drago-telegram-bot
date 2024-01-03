from pydantic import BaseModel


class BaseToken(BaseModel):
    address: str
    name: str
    symbol: str


class Liquidity(BaseModel):
    base: int | float
    quote: int | float
    usd: int | float


class PriceChange(BaseModel):
    h1: float
    h6: float
    h24: float
    m5: float


class QuoteToken(BaseModel):
    address: str
    name: str
    symbol: str


class BuysAndSells(BaseModel):
    buys: int
    sells: int


class Txns(BaseModel):
    h1: BuysAndSells
    h6: BuysAndSells
    h24: BuysAndSells
    m5: BuysAndSells


class Volume(BaseModel):
    h1: float
    h6: float
    h24: float
    m5: float


class Token(BaseModel):
    baseToken: BaseToken
    chainId: str
    dexId: str
    fdv: int
    liquidity: Liquidity
    pairAddress: str
    pairCreatedAt: int
    priceChange: PriceChange
    priceNative: str
    priceUsd: str
    quoteToken: QuoteToken
    txns: Txns
    url: str
    volume: Volume


class Tokens(BaseModel):
    pairs: list[Token]
    schemaVersion: str
