from flask import Flask, request, render_template
from openai import OpenAI
from prompts import PROMPTS  # Import prompts from a separate file
from collections import Counter


# Initialize Flask app
app = Flask(__name__)

# API keys and model endpoints
MODEL_CONFIG = {
    "llama": {
        "api_key": "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",  # Replace with Llama API key
        "endpoint": "meta/llama-3.1-8b-instruct"
    },
    "mistral": {
        "api_key": "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",  # Replace with Mistral API key
        "endpoint": "mistralai/mistral-7b-instruct-v0.2"
    }
}

# from collections import Counter

def generate_answer(model, dataset, prompting, user_table, user_query):
    # Select API key and endpoint for the model
    model_config = MODEL_CONFIG[model]
    client = OpenAI(
        base_url="https://integrate.api.nvidia.com/v1",
        api_key=model_config["api_key"]
    )

    # Select the appropriate fixed prompt (CoT and Self-Consistency share the same prompt)
    fixed_prompt = PROMPTS[dataset]["cot"]  # Using CoT prompt for self-consistency

    # Construct the input prompt
    input_prompt = f"{fixed_prompt}\nTable:\n{user_table}\n\nQuery: {user_query}\nAnswer:"

    try:
        # Check if prompting method is self-consistency
        if prompting == "self-consistency":
            # Sample multiple reasoning paths (n completions)
            completion = client.chat.completions.create(
                model=model_config["endpoint"],
                messages=[{"role": "user", "content": input_prompt}],
                temperature=0.7,  # Higher temperature for diverse outputs
                top_p=1,
                max_tokens=1024,
                n=5,  # Generate 5 different reasoning paths
                stream=False
            )

            # Collect all responses
            answers = [choice.message.content.strip() for choice in completion.choices]

            # Find the most consistent answer using majority vote
            final_answer = Counter(answers).most_common(1)[0][0]
            return final_answer

        else:
            # Standard single-path reasoning for direct or CoT
            completion = client.chat.completions.create(
                model=model_config["endpoint"],
                messages=[{"role": "user", "content": input_prompt}],
                temperature=0.5,
                top_p=1,
                max_tokens=1024,
                stream=False
            )

            # Extract and return the response content
            return completion.choices[0].message.content.strip()

    except Exception as e:
        # Handle API errors gracefully
        return f"Error generating answer: {str(e)}"




# Routes
@app.route("/", methods=["GET", "POST"])
def index():
    # Default values
    model = "llama"
    dataset = "fetaqa"
    prompting = "direct"
    table = ""
    query = ""
    answer = ""

    if request.method == "POST":
        # Get values from the form
        model = request.form.get("model", "llama")
        dataset = request.form.get("dataset", "fetaqa")
        prompting = request.form.get("prompting", "direct")
        table = request.form.get("table", "")
        query = request.form.get("query", "")
        
        # Generate answer if table and query are provided
        if table and query:
            answer = generate_answer(model, dataset, prompting, table, query)
    
    # Render the template with all values
    return render_template("index.html", model=model, dataset=dataset, prompting=prompting, table=table, query=query, answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
