from pydantic import BaseModel
from typing import List

class PilotData(BaseModel):
    name: str
    lap_times: List[float]

class IQRResponse(BaseModel):
    iqr: float
    pilots: List[PilotData]
