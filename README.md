# ActiveSG Gym Capacity API

A simple Flask API that scrapes and provides real-time capacity information for ActiveSG gyms in Singapore.

## Description

This API fetches the current capacity information for all ActiveSG gyms from the official ActiveSG website and presents it in a clean JSON format. It uses Cloudscraper to bypass any potential anti-bot measures.

## Features

- Returns capacity information for all ActiveSG gyms in Singapore
- Simple RESTful API design
- Bypasses Cloudflare anti-bot protection

## API Endpoints

- `GET /`: Welcome message
- `GET /api/gym-capacity`: Returns current capacity information for all ActiveSG gyms

## Sample Response

```json
{
  "Bedok ActiveSG Gym": 35,
  "Bishan ActiveSG Gym": 55,
  ...
}
```

## Requirements

- Python
- Flask
- cloudscraper

## Installation

1. Clone this repository
2. Install dependencies:
   ```
   pip install flask cloudscraper
   ```
3. Run the application:
   ```
   python app.py
   ```

The API will be available at http://localhost:10000

## Deployment

The app is configured to run on port 10000 by default, but will use the PORT environment variable if available.

## License

[MIT](LICENSE)
