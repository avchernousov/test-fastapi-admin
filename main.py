from fastapi_admin.factory import app as admin_app

def create_app():
    fast_app = FastAPI(debug=False)
    register_tortoise(fast_app, config=TORTOISE_ORM)
    fast_app.mount("/admin", admin_app)
    return fast_app


app = create_app()


@app.on_event("startup")
async def start_up():
    await admin_app.init(  # nosec
        admin_secret="test",
        permission=True,
        admin_log=True,
        site=Site(
            name="FastAPI-Admin DEMO",
            login_footer="FASTAPI ADMIN - FastAPI Admin Dashboard",
            login_description="FastAPI Admin Dashboard",
            locale="en-US",
            locale_switcher=True,
            theme_switcher=True,
        ),
    )


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, debug=False, reload=False, lifespan="on")
