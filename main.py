from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from forward import router as forward_router
from reverse import router as reverse_router

app = FastAPI(
    title="FastAPI-Geocode",
    description="Forward and Reverse Geocoding API",
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(forward_router)
app.include_router(reverse_router)
