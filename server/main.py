import logging
from fastapi import FastAPI
import uvicorn
from api.models import product_model
from api.database import engine
from api.routers.product import router as product_router

app = FastAPI(title="PyTaskManager", version="1.0.0",
              summary="A very basic API as a result of a personal experiment with FastAPI",
              contact={"name": "Navid Jalili", "url": "https://github.com/Navid-JL#-contact", "email": "navidjalili3@gmail.com"}, license_info={"name": "CC0 1.0 Universal"})

product_model.Base.metadata.create_all(engine)

app.include_router(product_router, prefix="/product", tags=["Product"])

logging.basicConfig(
    filename="./api/logs/app.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

if __name__ == '__main__':
    uvicorn.run('main:app', port=5000, reload=True,
                server_header=False, headers=[("x-server", "BinaryAPI")])
