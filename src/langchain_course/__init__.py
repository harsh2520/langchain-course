import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def main() -> None:
    print("Hello from langchain-course!")
    print(os.getenv("OPEN_API_KEY"))

if __name__ == "__main__":
    main()