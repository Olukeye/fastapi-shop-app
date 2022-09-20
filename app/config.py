from pydantic import BaseSettings

class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minute: int
    # email: str
    # email_password: str
    # flw_secret_key: str
    # flw_encryption_key: str
    # flw_public_key: str
    
    
    class Config:
        env_file = ".env"

settings = Settings()