# line-hackathon-chatui

A simple FastAPI web server for the Line Hackathon Chat UI project.

## Features

- FastAPI-based REST API
- Root endpoint with welcome message
- Health check endpoint

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Esther125/line-hackathon-chatui.git
cd line-hackathon-chatui
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Server

Start the server with:
```bash
uvicorn main:app --reload
```

The server will be available at `http://127.0.0.1:8000`

## API Endpoints

- `GET /` - Root endpoint returning a welcome message
- `GET /health` - Health check endpoint
- `GET /docs` - Interactive API documentation (Swagger UI)
- `GET /redoc` - Alternative API documentation (ReDoc)

## Development

The server runs in development mode with auto-reload enabled. Any changes to the code will automatically restart the server.