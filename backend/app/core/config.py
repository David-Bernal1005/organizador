import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    SECRET_KEY: str = os.getenv("SECRET_KEY", "change_me")
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", 
        "mysql+pymysql://root:YlsazmheiumkUvbntpcGzGzXhDnxllTb@switchyard.proxy.rlwy.net:38309/railway"
    )

settings = Settings()