from pydantic import BaseModel, EmailStr, SecretStr


class AccountRequest(BaseModel):
    email: EmailStr
    password: SecretStr
