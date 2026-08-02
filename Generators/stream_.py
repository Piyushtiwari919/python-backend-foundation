from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

#Give Generator
stream = client.responses.create(
    model="gpt-5.6",
    input=[
        {
            "role": "user",
            "content": "Say 'double bubble bath' ten times fast.",
        },
    ],
    stream=True,
)


def main() -> None:
    for chunk in stream:
        print(chunk)

if __name__ == "__main__":
    main()
