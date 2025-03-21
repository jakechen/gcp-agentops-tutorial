import os
from google import genai

PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT")
LOCATION = os.environ.get("GOOGLE_CLOUD_REGION", "us-central1")
MODEL_ID = "gemini-2.0-flash"

client = genai.Client(vertexai=True, project=PROJECT_ID, location=LOCATION)


def main(prompt):
    response = client.models.generate_content(model=MODEL_ID, contents=prompt)
    print(response.text)


if __name__ == "__main__":
    prompt = "What's the largest planet in our solar system?"
    main(prompt)
