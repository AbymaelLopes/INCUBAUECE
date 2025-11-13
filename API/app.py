import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/', response_class=FileResponse)
async def root():
    return 'static/index.html'

if __name__ == "__main__":
    uvicorn.run("app:app", port=8000, reload=True)