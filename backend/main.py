from fastapi import FastAPI

app = FastAPI(title="IA-ARMY — vitrine")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
