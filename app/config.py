from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(__file__).parent / ".env"

load_dotenv(env_path)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")