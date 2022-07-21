from dotenv import load_dotenv
from os import getenv

load_dotenv()

PRIVATE_KEY = getenv("PRIVATE_KEY")
INFURA_URL = getenv("INFURA_URL")