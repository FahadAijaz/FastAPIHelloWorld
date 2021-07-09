from fastapi import FastAPI
from hello import Hello
# some comment
app = FastAPI()
@app.get("/")
async def hello():
    hello = Hello(some_str = 'good')
    return {'message': hello.some_str}