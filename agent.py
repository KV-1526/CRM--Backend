import os
import json
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("❌ GROQ API KEY NOT FOUND")

# ✅ Working model
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=api_key
)

def process_message(message: str):
    try:
        prompt = f"""
Extract CRM details from the message.

Return ONLY valid JSON (no explanation).

Format:
{{
  "doctor": "",
  "hospital": "",
  "notes": "",
  "follow_up": ""
}}

Message:
{message}
"""

        response = llm.invoke(prompt)

        content = response.content if hasattr(response, "content") else str(response)

        # ✅ Convert to JSON safely
        try:
            return json.loads(content)
        except:
            return {
                "doctor": "",
                "hospital": "",
                "notes": content,
                "follow_up": ""
            }

    except Exception as e:
        return {
            "doctor": "",
            "hospital": "",
            "notes": f"Error: {str(e)}",
            "follow_up": ""
        }