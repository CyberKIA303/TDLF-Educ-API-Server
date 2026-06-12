import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from fastapi import FastAPI
from backend import (get_all_routes, create_tables)
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title = "TDLF-Educ",
    description = "This API is Specialize on Education Only",
    version = "1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

routes = get_all_routes()
for route in routes:
    app.include_router(route)
    
@app.on_event("startup")
async def startup():
    create_tables()
    print("TDLF-Educ API Open!")

@app.on_event("shutdown")
async def shutdown():
    print("TDLF-Educ API Closed!")