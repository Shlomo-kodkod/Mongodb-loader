from fastapi import FastAPI 
from fastapi.responses import JSONResponse
import logging
from service.dal import DataLoader


app = FastAPI()
logger = logging.getLogger(__name__)

@app.get("/names")
def get_names():
    """
    Endpoint to retrieve student from the database.
    Returns the data or an error message if the retrieval fails.
    """
    try:
        data = DataLoader.load_data()
        logger.info("Data received successfully")
        return JSONResponse(content=data)
    except Exception as e:
        logger.error("Error while receiving data")
        return JSONResponse(content={"Error": e})
    

        