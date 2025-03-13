from fastapi import APIRouter, HTTPException
from services.fastf1_service import get_lap_times_iqr

router = APIRouter()


@router.get("/iqr/{season}/{gp}/{drivers}")
async def calculate_iqr(season: int, gp: int, drivers: str):
    driver_list = drivers.split(',')
    try:
        iqr_data = get_lap_times_iqr(season, gp, driver_list)
        return {"iqr": iqr_data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
