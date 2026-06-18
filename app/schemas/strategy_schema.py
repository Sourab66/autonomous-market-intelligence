from pydantic import BaseModel
from typing import List


class StrategyReport(BaseModel):

    target_audience: str

    marketing_channels: List[str]

    positioning: str

    recommendations: List[str]