import gradio as gr
from app.utils import broken_telephone, generate_image, describe_image

def run_broken_telephone(initial_prompt, n_rounds):
    """
    Wrapper function to run the broken telephone game and return results.
    """
    results = []
    current_prompt = initial_prompt

    for i in range(n_rounds):
        result = {
            "round": i + 1,
            "prompt": current_prompt,
        }
        # Generate an image from the current prompt
        b64_image = generate_image(current_prompt)
        result["image"] = b64_image

        # Describe the generated image
        current_prompt = describe_image(b64_image)
        result["description"] = current_prompt

        results.append(result)

    return results

# Gradio Interface
def gradio_interface(initial_prompt, n_rounds):
    results = run_broken_telephone(initial_prompt, n_rounds)
    output = ""
    for result in results:
        output += f"### Round {result['round']}\n"
        output += f"**Prompt:** {result['prompt']}\n"
        output += f"**Description:** {result['description']}\n"
        output += f"![Image](data:image/png;base64,{result['image']})\n\n"
    return output

# Create Gradio Interface
interface = gr.Interface(
    fn=gradio_interface,
    inputs=[
        gr.Textbox(label="Initial Prompt", placeholder="Enter your initial prompt here"),
        gr.Slider(label="Number of Rounds", minimum=1, maximum=10, step=1, value=3),
    ],
    outputs=gr.Markdown(label="Broken Telephone Results"),
    title="Broken Telephone Game",
    description="Enter an initial prompt and specify the number of rounds to play the Broken Telephone game.",
)

# Launch the Gradio App
if __name__ == "__main__":
    interface.launch()