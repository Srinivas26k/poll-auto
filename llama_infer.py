from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='ollama'
)

def generate_poll(transcript):
    prompt = f"""
    Based on this conversation excerpt, generate a poll question and 4 multiple choice options (no explanations).

    Transcript:
    \"\"\"
    {transcript}
    \"\"\"

    Return in this JSON format:
    {{
      "question": "...",
      "options": ["...", "...", "...", "..."]
    }}
    """

    response = client.chat.completions.create(
        model="llama3.2:latest",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    reply = response.choices[0].message.content

    try:
        parsed = eval(reply)  # Ollama may return Python-style dicts
        return parsed["question"], parsed["options"]
    except:
        print("⚠️ Failed to parse LLaMA response:")
        print(reply)
        return "What did we discuss?", ["Option A", "Option B", "Option C", "Option D"]
