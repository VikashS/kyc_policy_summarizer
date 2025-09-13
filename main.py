import os
from dotenv import load_dotenv

load_dotenv()

def main():
    print("Hello from kyc-policy-summarizer!")
    res=os.environ.get("OPENAI_API_KEY")
    print(res)


if __name__ == "__main__":
    main()
