from fastapi import FastAPI
from controllers.movies_controller import movie_router
from fastapi.middleware.cors import CORSMiddleware

# Create and configure FastAPI app
app = FastAPI()
app.title = "Movies catalog application"
app.version = "0.0.1"

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Create main routes
@app.get("/", tags=["Main"])
async def root():
    return "Movies server running!"


@app.get("/api/v1", tags=["Main"])
async def say_welcome_api():
    return "Welcome to the movies REST API V1!"

# Include other routers
app.include_router(movie_router, prefix="/api/v1")
