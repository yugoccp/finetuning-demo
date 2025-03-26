import base64
from pdf2image import convert_from_path
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def encode_image(image):
    from io import BytesIO
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

def extract_text_and_images(pdf_path):
    return convert_from_path(pdf_path)

def analyze_with_openai(image_base64):
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Describe the details and content of this image."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_base64}"
                        }
                    }
                ]
            }
        ]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    
    pdf_file = "../data/yugioh_rulebook.pdf"
    images = extract_text_and_images(pdf_file)

    print(f"Analyze image and saving content...")
    
    output_file = "../data/yugioh_rulebook.md"
    with open(output_file, 'a', encoding='utf-8') as file:
        for idx, img in enumerate(images):
            image_base64 = encode_image(img)

            # Analyze each page individually
            analysis_result = analyze_with_openai(image_base64)
                
            print("=== GPT-4 Vision Analysis Result ===")
            print(analysis_result)
            print("\n")

            # Append model result into output file
            file.write(f"""\
            ---
            # Image {idx}
            {analysis_result}
            """)

