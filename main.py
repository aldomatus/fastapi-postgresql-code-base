from functools import lru_cache
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.core.config import Settings
from app.api.api_v1.api import api_router

settings = Settings()
app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Webookyou backend",
    version="0.0.1",
    openapi_tags=[
        {
            "name": "user",
            "description": "users routes"
        }
    ],
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)


@lru_cache()
def get_settings():
    return Settings()


app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get('/', response_class=RedirectResponse, include_in_schema=False)
async def docs():
    return RedirectResponse(url='/docs')
