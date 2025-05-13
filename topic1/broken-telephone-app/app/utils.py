import os
import base64
import json
from openai import OpenAI
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

with open("nebius_api_key", "r") as file:
    nebius_api_key = file.read().strip()

os.environ["NEBIUS_API_KEY"] = nebius_api_key

# Initialize the OpenAI client
client = OpenAI(
    base_url="https://api.studio.nebius.ai/v1/",
    api_key=os.environ.get("NEBIUS_API_KEY"),
)

# Function to generate an image from a text prompt
def generate_image(prompt, model="black-forest-labs/flux-dev"):
    response = client.images.generate(
        model=model,
        response_format="b64_json",
        extra_body={
            "response_extension": "png",
            "width": 512,
            "height": 512,
            "num_inference_steps": 28,
            "negative_prompt": "",
            "seed": -1,
        },
        prompt=prompt,
    )
    response_json = response.to_json()
    response_data = json.loads(response_json)
    b64_image = response_data["data"][0]["b64_json"]
    return b64_image

# Function to describe an image using a multimodal LLM
def describe_image(b64_image, model="Qwen/Qwen2-VL-72B-Instruct"):
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are an expert image describer."},
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Describe the content of this image."},
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64_image}"}},
                ],
            },
        ],
    )
    return completion.choices[0].message.content

# Function to decode and display a base64 image
def display_image(b64_image):
    image_bytes = base64.b64decode(b64_image)
    image = Image.open(BytesIO(image_bytes))
    plt.imshow(image)
    plt.axis("off")
    plt.show()

# Broken telephone game
def broken_telephone(initial_prompt, n_rounds=5):
    current_prompt = initial_prompt
    for i in range(n_rounds):
        print(f"Round {i + 1}:")
        print(f"Prompt: {current_prompt}")
        
        # Generate an image from the current prompt
        b64_image = generate_image(current_prompt)
        display_image(b64_image)
        
        # Describe the generated image
        current_prompt = describe_image(b64_image)
        print(f"Description: {current_prompt}")
        print("-" * 50)