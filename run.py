import uvicorn
from config import init_config, API_HOST, API_PORT

if __name__ == "__main__":
    init_config()
    uvicorn.run("main:app", host=API_HOST, port=API_PORT, reload=True)
