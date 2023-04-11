from fastapi import FastAPI
from src.database import engine, Base
from src.routers.movie_router import movie_router

# Create and configure FastAPI app
app = FastAPI()
app.title = "Movies catalog application"
app.version = "0.0.1"

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(movie_router, prefix="/api/v1")


# Create main routes
@app.get("/", tags=["Main"])
async def root():
    return "<p>Movies server running!</p>"


@app.get("/api/v1", tags=["Main"])
async def say_welcome_api():
    return "<p>Welcome to the movies REST API V1!</p>"

