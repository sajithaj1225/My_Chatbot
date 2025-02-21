# app.py
from flask import Flask, render_template, request, jsonify
from groq import Groq

# Initialize the Groq client with your API key
api_key = "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"  # Replace with your actual API key
client = Groq(api_key=api_key)

app = Flask(__name__)

def format_response(response_text):
    # Split by numbers or bullet points and wrap each in a <li> tag
    import re
    lines = re.split(r'\d+\.\s|\n|\*|\-', response_text)
    formatted_text = "<ul>"
    for line in lines:
        if line.strip():
            formatted_text += f"<li>{line.strip()}</li>"
    formatted_text += "</ul>"
    return formatted_text


# Function to get response from Groq
def get_groq_response(user_input):
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": user_input}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()  # Correctly parse JSON data
    user_message = data.get("user_message")
    bot_response = get_groq_response(user_message)
    return jsonify({"bot_response": bot_response})


if __name__ == "__main__":
    app.run(debug=True)

# Instructions:
# - Save this code in `app.py`.
# - Create a separate `templates` folder and place your `index.html` inside it.
# - Create a `static` folder for your CSS and JS files.

# Sample index.html and CSS code provided separately.