from fastapi import FastAPI

app = FastAPI(title="Line Hackathon Chat UI", version="1.0.0")


@app.get("/")
async def root():
    """Root endpoint returning a welcome message."""
    return {"message": "Welcome to Line Hackathon Chat UI API"}


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}
