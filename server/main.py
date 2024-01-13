import logging
from fastapi import FastAPI
import uvicorn
from api.models import product_model
from api.database import engine

app = FastAPI(title="PyTaskManager")

product_model.Base.metadata.create_all(engine)

logging.basicConfig(
    filename="./api/logs/app.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

if __name__ == '__main__':
    uvicorn.run('main:app', port=5000, reload=True,
                server_header=False, headers=[("x-server", "BinaryAPI")])
