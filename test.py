from openai import OpenAI

# Test API key and endpoint
try:
    client = OpenAI(
        base_url="https://integrate.api.nvidia.com/v1",
        api_key="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"  # Replace with your key
    )

    response = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct-v0.2",  # Test with Llama endpoint
        messages=[{"role": "user", "content": "Test message"}],
        max_tokens=50
    )

    print(response)
except Exception as e:
    print("Error:", e)
