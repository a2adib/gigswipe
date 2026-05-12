from fastapi import FastAPI

app = FastAPI(title="GigSwipe")

@app.get("/")
async def root():
    return {"message": "GigSwipe API - Step 1 complete"}