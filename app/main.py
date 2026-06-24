from fastapi import FastAPI

app = FastAPI(
    title="AI Investment Research Agent"
)

@app.get("/")
def home():
    return {
        "message": "AI Investment Research Agent Running"
    }