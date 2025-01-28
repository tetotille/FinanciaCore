from fastapi import FastAPI
import os

app = FastAPI()

# Middleware opcional para desarrollo
if os.getenv("ENV") == "development":
    from debug_toolbar.middleware import DebugToolbarMiddleware
    app.add_middleware(DebugToolbarMiddleware)

@app.get("/")
async def root():
    return {"message": "Welcome to FinanciaCore!"}
