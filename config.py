from os import getenv
from dotenv import load_dotenv

load_dotenv()

PORT = getenv("PORT", 5000)
