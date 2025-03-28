from dotenv import load_dotenv
import os

load_dotenv()
print("OPENAI_API_KEY =", os.environ.get("OPENAI_API_KEY"))