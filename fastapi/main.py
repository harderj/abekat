
import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.responses import HTMLResponse

html_path = r"C:\repos\abekat\fastapi\html\abe.html"
router = APIRouter()

@router.get("/abe", response_class=HTMLResponse)
def get_abe():
    cnt : str
    with open(html_path, mode='r') as file:
        cnt = file.read()
    # cnt = "abe"
    return cnt

app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
   uvicorn.run(app, host='0.0.0.0', port=8000)

