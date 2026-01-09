from src.client import app
from uvicorn import run

def main():
    run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
