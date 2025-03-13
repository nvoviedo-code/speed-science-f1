# Speed Science F1 Application

This project is a FastAPI application that utilizes the FastF1 library to query Formula 1 data and provides an endpoint for calculating the lap speed based on Interquartile Range (IQR) metric for a list of drivers for a specified Grand Prix.

## Project Structure

```
speed-science-f1
├── src
│   ├── main.py                # Entry point of the FastAPI application
│   ├── routers
│   │   └── fastf1_router.py   # Routing setup for the application
│   ├── services
│   │   └── fastf1_service.py  # Logic for interacting with the FastF1 library
│   └── custom_types
│       └── __init__.py        # Custom types and data models
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd speed-science-f1
   ```

2. Create a virtual environment:
   ```
   python -m venv ssf1-venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     ssf1-venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source ssf1-venv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the Speed Science F1 application, execute the following command:
```
uvicorn src.main:app --reload
```

You can access the API documentation at `http://127.0.0.1:8000/docs`.

## Endpoints

- **Calculate IQR for Drivers**
  - **Endpoint:** `/iqr/{season}/{gp}/{drivers}`
  - **Method:** `GET`
  - **Path Parameters:**
    - `season`: The season year (e.g., 2021).
    - `gp`: The round number of the Grand Prix (e.g., 1 for the first GP).
    - `drivers`: A comma-separated list of driver codes (e.g., `HAM,VER`).
  - **Response:** JSON object containing the calculated IQR for the specified drivers.

### Example

To calculate the lap speed based on IQR metric for drivers Hamilton and Verstappen in the first GP of the 2021 season, you can use the following URL:
```
http://127.0.0.1:8000/iqr/2021/1/HAM,VER
```

The response will be a JSON object like this:
```json
{
    "HAM": 1.234,
    "VER": 1.567
}
```

## License

This project is licensed under the MIT License.
