from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


#import hug
#@hug.get("/")
#def health_check():
#    return {
#        "message": "Good."
#    }