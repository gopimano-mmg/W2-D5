from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7,
)

prompt = """
Suggest exactly 5 healthy breakfast ideas.
Include protein and fibre-rich ingredients.
Keep added sugar low.
Use a numbered list from 1 to 5, one idea per line.
Do not include an introduction, conclusion, or extra text.
"""

reply = llm.invoke(prompt)

# First, inspect the message object.
# Print only the reply text.
print(reply.content)