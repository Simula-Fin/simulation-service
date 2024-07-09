from pydantic import BaseModel, EmailStr, field_validator
from datetime import datetime, date
from enum import Enum

class BaseRequest(BaseModel):
    # may define additional fields or config shared across requests
    pass


class RefreshTokenRequest(BaseRequest):
    refresh_token: str


class UserUpdatePasswordRequest(BaseRequest):
    password: str


class CalculationMethod(str, Enum):
    sac = "sac"
    price = "price"

class UserCreateRequest(BaseRequest):
    email: EmailStr
    password: str
    name: str
    telephone: str
    monthly_income: float
    cpf: str
    birth_date: date
    pix_key: str


class LoanSimulationRequest(BaseRequest):
    amount: float
    duration_months: int
    tax: float
    calculation_method: CalculationMethod

class ConsortiumSimulationRequest(BaseRequest):
    amount: float
    duration_months: int
    tax: float
    calculation_method: CalculationMethod

class FinancingSimulationRequest(BaseRequest):
    amount: float
    duration_months: int
    tax: float  
    calculation_method: CalculationMethod  

class RSAEncryptRequest(BaseModel):
    message: str
    public_key: str

class RSADecryptRequest(BaseModel):
    message: str
    private_key: str

class ChatBotRequest(BaseModel):
    prompt: str
    model: str = "gpt-3.5-turbo"
    max_tokens: int = 2048
    temperature: float = 0.5