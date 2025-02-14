from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost",
    "http://20.109.44.129",
    "http://localhost:3000",
    "http://20.109.44.129:3000",
    "http://localhost:3001",
    "http://20.109.44.129:3001",
    "https://quivr.app",
    "https://www.quivr.app",
    "http://quivr.app",
    "http://www.quivr.app",
    "*",
]


def add_cors_middleware(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
