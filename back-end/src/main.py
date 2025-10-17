from contextlib import asynccontextmanager

from fastapi import FastAPI
from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka

from src.di import (
    DatabaseProvider,
    ConfigurationProvider,
    InfrastructureProvider,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await app.state.dishka_container.close()


container = make_async_container(
    DatabaseProvider(),
    ConfigurationProvider(),
    InfrastructureProvider(),
)

app = FastAPI(lifespan=lifespan)
setup_dishka(container=container, app=app)
