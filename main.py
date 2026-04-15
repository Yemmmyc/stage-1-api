from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/health")
def health():
    return {"message": "healthy"}

@app.get("/me")
def me():
    return {
        "name": "Oluwayemisi Okunrounmu",
        "email": "yemmmyc@hotmail.com",
        "github": "https://github.com/Yemmmyc"
    }