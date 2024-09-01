import logging

from fastapi import FastAPI, Request
from .endpoints import router


app = FastAPI()

app.include_router(router)

logger = logging.getLogger()


@app.middleware("http")
async def log_middleware(request: Request, call_next):
    logger.info(
        f"REQUEST START: {request.method} {request.url} from {request.client.host}"
    )
    response = await call_next(request)
    logger.info(
        f"REQUEST END: {request.method} {request.url} from {request.client.host}"
    )
    return response
