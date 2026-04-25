from pydantic import BaseModel, Field
from datetime import datetime


class Medicao(BaseModel):
    corrente: float
    tensao: float
    potencia: float
    timestamp: datetime | None = None
