from starlette.config import Config

config = Config(".env")

# general settings
PROJECT_NAME: str = config("PROJECT_NAME", default="whois-rest")

DEBUG: bool = config("DEBUG", cast=bool, default=False)
TESTING: bool = config("TESTING", cast=bool, default=False)
