from fastapi import APIRouter

entry_root = APIRouter()

# endpoint's
@entry_root.get("/")
def api_running():
     res = {
          "status": "running",
          "message": "api is running"
     }
     
     return res