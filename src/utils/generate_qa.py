from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


def generate_qa(content):
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": """
You are a data preparation assistant helping to generate training data for fine-tuning a language model.

Given the following section of text, generate 20 unique question-and-answer (Q&A) pairs that comprehensively cover all key ideas, facts, and concepts in the text.

Requirements:
•	Each question should test understanding of a different point or concept from the text.
•	Avoid duplicating question types or topics.
•	Answers should be complete, accurate, and concise, based only on the given text.
•	Questions should vary in style (e.g., factual, conceptual, inference-based) to create a diverse dataset.
•	Format the output as a list of 20 JSON objects, each with the structure:
{
    "question": "...",
    "answer": "..."
}

Text Section:
""" + content
            }
        ]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":

    print(f"==== Generate Q&A ====")

    # Split content by pages
    content_file = "./data/outputs/yugioh_rulebook_image.md"
    with open(content_file, 'r', encoding='utf-8') as file:
        pages = [page for page in file.read().split('---') if page.strip()]

    # Generate Q&A samples for each page and aggregate in single file
    output_file = "./data/outputs/yugioh_rulebook_qa600.json"
    with open(output_file, 'a', encoding='utf-8') as file:
        for page in pages:
            page_qa = generate_qa(page)
            file.write(f"\n{page_qa}")

