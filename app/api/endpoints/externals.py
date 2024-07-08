from fastapi import APIRouter
from app.schemas.requests import RSAEncryptRequest, RSADecryptRequest
import requests
from fastapi import HTTPException

router = APIRouter()

@router.post("/rsa/encrypt", description="Encrypt RSA keys")
async def generate_rsa_keys(request: RSAEncryptRequest):
    try:
        response = requests.post(
            "https://5a7udyuiimjx3rngjs7lp4dxee0phmbl.lambda-url.us-east-1.on.aws/rsa/encrypt",
            json=request.dict()
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return {"status": "Request sent", "response": response.json()}


@router.post("/rsa/decrypt", description="decrypt RSA keys")
async def generate_rsa_keys(request: RSADecryptRequest):
    try:
        response = requests.post(
            "https://5a7udyuiimjx3rngjs7lp4dxee0phmbl.lambda-url.us-east-1.on.aws/rsa/decrypt",
            json=request.dict()
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return {"status": "Request sent", "response": response.json()}
