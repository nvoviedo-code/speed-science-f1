import fastf1
import pandas as pd
import numpy as np
import logging

from settings import CACHE_LOCATION

# Enable debug logging
logging.basicConfig(level=logging.DEBUG)


def get_lap_times_iqr(season: int, gp: int, drivers: list):
    """
    Calculate the Interquartile Range (IQR) of lap times for a list of drivers in a given Grand Prix.

    Parameters:
    season (int): The season year (e.g., 2021).
    gp (int): The round number of the Grand Prix (e.g., 1 for the first GP).
    drivers (list): A list of driver codes (e.g., ['HAM', 'VER']).

    Returns:
    dict: A dictionary with driver codes as keys and their respective IQR of lap times as values.
          If no lap times are found for a driver, the value will be None.
    """
    try:
        fastf1.Cache.enable_cache(CACHE_LOCATION)  # Enable caching
        session = fastf1.get_session(season, gp, 'R')
        session.load()

        iqr_data = {}
        drivers_laps = session.laps.pick_drivers(drivers)
        
        for driver in drivers:
            lap_times = drivers_laps[drivers_laps['Driver'] == driver]['LapTime'].dt.total_seconds()

            if lap_times.empty:
                iqr_data[driver] = None
            else:
                lap_times_series = pd.Series(lap_times)
                Q1 = lap_times_series.quantile(0.25)
                Q3 = lap_times_series.quantile(0.75)
                IQR = Q3 - Q1
                # Replace NaN values with None
                iqr_data[driver] = None if np.isnan(IQR) else IQR

        return iqr_data
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise
