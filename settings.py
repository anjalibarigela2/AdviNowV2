import os
from dotenv import load_dotenv

load_dotenv()


def get_env(variable_name, default=None):
    value = os.getenv(variable_name, default)
    if value and str(value).lower() in ("true", "false"):
        return str(value).lower() == "true"
    return value


# Postgres
DB_HOST = get_env("DB_HOST", "127.0.0.1")
DB_NAME = get_env("DB_NAME", "Advinow")
DB_USER = get_env("DB_USER", "postgres")
DB_PASSWORD = get_env("DB_PWD", "Anju123@")

DB_URL: str = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}?sslmode=disable"
