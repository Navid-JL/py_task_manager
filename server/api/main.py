import logging
from fastapi import FastAPI
import uvicorn

app = FastAPI(title="PyTaskManager")

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

if __name__ == '__main__':
    uvicorn.run('main:app', port=5000, reload=True,
                server_header=False, headers=[("x-server", "BinaryAPI")])
