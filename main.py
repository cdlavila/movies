from fastapi import FastAPI
from controllers.auth_controller import auth_router
from controllers.users_controller import users_router
from controllers.directors_controller import directors_router
from controllers.movies_controller import movies_router
from fastapi.middleware.cors import CORSMiddleware

# Create and configure FastAPI app
app = FastAPI()
app.title = "Movies Catalog Application"
app.version = "1.0.0"
app.description = "This is a simple REST API application for movies catalog"

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Create main routers
@app.get("/", tags=["Main"])
async def root():
    return "Movies server running!"


@app.get("/api/v1", tags=["Main"])
async def say_welcome_api():
    return "Welcome to the movies REST API V1!"

# Include other routers
app.include_router(auth_router, prefix="/api/v1")
app.include_router(users_router, prefix="/api/v1")
app.include_router(directors_router, prefix="/api/v1")
app.include_router(movies_router, prefix="/api/v1")
