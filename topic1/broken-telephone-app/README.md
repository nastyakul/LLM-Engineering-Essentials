# Broken Telephone Game Web Application

This project implements a web application for the "Broken Telephone" game using a multimodal LLM and image generation. The application is now built using **Gradio** for an interactive and user-friendly interface. It is designed to be run in Google Colab or locally.

## Project Structure

```
broken-telephone-app
├── app
│   ├── __init__.py
│   ├── utils.py
├── gradio_app.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the Repository**: 
   Clone this repository to your local machine or Google Drive.

2. **Install Dependencies**: 
   Open a new Colab notebook or terminal and run the following command to install the required libraries:
   ```python
   !pip install -r requirements.txt
   ```

3. **Run the Application**: 
   Execute the following command in a new cell or terminal to start the Gradio app:
   ```python
   !python gradio_app.py
   ```

4. **Access the Application**: 
   Once the app is running, a URL will be displayed in the output. Open this URL in your browser to interact with the application.

## How to Use the Application

- Enter a text prompt to start the "Broken Telephone" game.
- Specify the number of rounds for the game.
- The application will generate an image based on the prompt and describe it using a multimodal LLM.
- The results, including images and descriptions, will be displayed in the Gradio interface.

## Example Usage

To start the game, you can use the following example prompt:
```python
initial_prompt = "An Amsterdam-based data scientist doing their work in their home office"
```

## Contributing

Feel free to fork the repository and submit pull requests for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.