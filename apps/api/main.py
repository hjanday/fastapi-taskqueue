"""FastAPI application entry point."""

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from .config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug,
)


@app.get("/")
async def root() -> JSONResponse:
    """Root endpoint returning basic API information."""
    return JSONResponse(
        content={
            "name": settings.app_name,
            "version": settings.app_version,
            "status": "healthy",
        }
    )


@app.get("/health")
async def health() -> JSONResponse:
    """Health check endpoint."""
    return JSONResponse(content={"status": "healthy"})
