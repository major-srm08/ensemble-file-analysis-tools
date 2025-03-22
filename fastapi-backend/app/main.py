from fastapi import FastAPI
from app.api.routes import router  # ✅ Import the router from routes.py

app = FastAPI(title="File Analysis API", description="API for analyzing files.")

# ✅ Include the API router
app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Welcome to the File Analysis API!"}

