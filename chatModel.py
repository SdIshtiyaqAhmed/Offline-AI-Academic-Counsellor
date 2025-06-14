from flask import Flask, render_template, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import pandas as pd
import os
import json

# Initialize Flask app
app = Flask(__name__)

# Auto-select device (use GPU if available)
device = "cpu"

# Load both models
from transformers import AutoModelForCausalLM, AutoTokenizer

device = "cpu"

# Paths
larger_model_path = "HuggingFaceTB/SmolLM2-360M-Instruct"
smaller_model_path = "HuggingFaceTB/SmolLM2-135M-Instruct"

# Load both
models = {
    "large": AutoModelForCausalLM.from_pretrained(larger_model_path).to(device),
    "small": AutoModelForCausalLM.from_pretrained(smaller_model_path).to(device)
}
tokenizers = {
    "large": AutoTokenizer.from_pretrained(larger_model_path),
    "small": AutoTokenizer.from_pretrained(smaller_model_path)
}

# Function to generate response
def generate_response(user_input, model_choice="small"):
    student_data = ""
    if os.path.exists(STUDENT_FILE):
        with open(STUDENT_FILE, "r") as file:
            student_records = [json.loads(line.strip()) for line in file if line.strip()]
            if student_records:
                student_data = f"My information:\n{json.dumps(student_records[-1], indent=2)}\n"

    system_prompt = "Your name is <b> AI Academic Counsellor </b>. You are a helpful AI academic counselor. Respond in HTML format using <br> for line breaks."
    if student_data:
        system_prompt += f"<br>Use the following data to provide personalized academic guidance:<br>{student_data}"

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ]

    # Select model + tokenizer
    model_key = "large" if model_choice == "large" else "small"
    tokenizer = tokenizers[model_key]
    model = models[model_key]

    input_text = tokenizer.apply_chat_template(messages, tokenize=False)
    inputs = tokenizer.encode(input_text, return_tensors="pt").to(device)

    outputs = model.generate(inputs, max_new_tokens=1000, temperature=0.7, top_p=0.9, do_sample=True)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    response_split = response.split("assistant\n")
    formatted_response = response_split[-1].strip() if len(response_split) > 1 else response.strip()
    
    return formatted_response

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Chatbot route
@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'GET':
        return render_template('chat.html')

    data = request.get_json()
    user_input = data.get("message", "").strip()
    model_choice = data.get("model", "small")  # default to small if not provided

    if not user_input:
        return jsonify({"response": "Please enter a valid message."}), 400

    response = generate_response(user_input, model_choice)
    return jsonify({"response": response})

# Quiz Route
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    file_path = "questions.xlsx"
    
    if not os.path.exists(file_path):
        return jsonify({"error": "Questions file not found"}), 500

    try:
        df = pd.read_excel(file_path)

        required_columns = {"Question", "Topic", "Difficulty", "Option 1", "Option 1 Score", "Option 2", "Option 2 Score", "Option 3", "Option 3 Score", "Option 4", "Option 4 Score", "Correct Answer", "Score"}
        if not required_columns.issubset(df.columns):
            return jsonify({"error": "Invalid Excel format. Required columns missing."}), 500

        if request.method == 'GET':
            return render_template('quiz.html')

        data = request.get_json()
        topic = data.get("topic", "").strip()

        if topic:
            df = df[df["Topic"].str.lower() == topic.lower()]
        
        if df.empty:
            return jsonify({"error": "No questions available for this topic"}), 404

        questions = df.to_dict(orient="records")

        quiz = []
        for q in questions:
            quiz.append({
                "question": q["Question"],
                "topic": q["Topic"],
                "options": [
                    {"text": q["Option 1"], "weight": q["Option 1 Score"]},  # Use "weight" instead of "score"
                    {"text": q["Option 2"], "weight": q["Option 2 Score"]},
                    {"text": q["Option 3"], "weight": q["Option 3 Score"]},
                    {"text": q["Option 4"], "weight": q["Option 4 Score"]},
                ],
                "correct_answer": q["Correct Answer"],
                "max_score": q["Score"]
            })

        return jsonify({"quiz": quiz})

    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

STUDENT_FILE = "student_records.jsonl"  # Store multiple records

@app.route('/save_scores', methods=['POST'])
def save_scores():
    data = request.json  # Get JSON data from the request

    # Write the data to a JSONL file
    with open(STUDENT_FILE, "w") as file:
        file.write(json.dumps(data) + "\n")

    return "Student record saved successfully!"

# Function to check if student exists
def get_existing_student():
    try:
        with open(STUDENT_FILE, "r") as file:
            for line in file:
                student = json.loads(line.strip())
                if "name" in student:
                    return student["name"]
    except FileNotFoundError:
        return None
    return None

@app.route("/check_student", methods=["GET", "POST"])
def check_student():
    if request.method == "GET":
        student_name = get_existing_student()
        if student_name:
            return jsonify({"exists": True, "name": student_name})
        return jsonify({"exists": False})

    elif request.method == "POST":
        data = request.get_json()
        student_name = data.get("name")

        if not student_name:
            return jsonify({"error": "Invalid name"}), 400

        with open(STUDENT_FILE, "a") as file:
            file.write(json.dumps({"name": student_name}) + "\n")
        
        return jsonify({"exists": True, "name": student_name, "message": f"Welcome, {student_name}!"})

# Run Flask App
if __name__ == '__main__':
    app.run(debug=True)