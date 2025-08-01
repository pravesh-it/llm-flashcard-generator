import openai

# Your provided API key (keep it private in real deployments!)
openai.api_key = "<Your_API_Key>"

def generate_flashcards(text, subject=None):
    prompt = f"""
Generate 15 question-answer flashcards from the following educational content.
{f"The subject is {subject}." if subject else ""}
Ensure questions are clear and answers are factual and self-contained.

Content:
{text}
"""
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert tutor creating Q&A flashcards."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content
