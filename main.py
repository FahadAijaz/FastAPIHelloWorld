from fastapi import FastAPI
# some comment
app = FastAPI()
@app.get("/")
async def hello():
    return {'message': 'hello'}