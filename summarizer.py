import openai

def generate_summary(transcript, openai_key):
    openai.api_key = openai_key

    prompt = (
        "You are an AI assistant. Summarize the following meeting transcript in a clear and concise way:\n\n"
        f"{transcript}\n\nSummary:"
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful meeting summarizer."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            temperature=0.5,
        )

        summary = response["choices"][0]["message"]["content"].strip()
        return summary

    except Exception as e:
        return f"OpenAI API error: {e}"
