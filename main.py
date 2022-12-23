import talon
import uvicorn

if __name__ == "__main__":
    talon.init()
    uvicorn.run("server.api:app", host="0.0.0.0", port=1000, reload=True)
